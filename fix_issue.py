import requests
import os
from tqdm import tqdm

def extract_repo_names_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    repo_names = []
    for line in lines:
        # Split the URL by '/' and get the last part as the repo name
        repo_name = line.strip().split('/')[-1]
        repo_names.append(repo_name)

    return repo_names

# Step 1: Get GitHub credentials from a file
with open('credentials.txt', 'r') as f:
    PAT = f.readline().strip()

headers = {
    'Authorization': f'token {PAT}',
    'Accept': 'application/vnd.github.v3+json'
}

# Extract repository names from the file
repo_names = extract_repo_names_from_file("repositories.txt")

for repo_name in tqdm(repo_names):
    # Step 2: For each repo, list all open issues
    response = requests.get(f'https://api.github.com/repos/insper-classroom/{repo_name}/issues', headers=headers, params={'state': 'open'})

    if response.status_code != 200:
        print(f"Error fetching issues for {repo_name}:", response.json().get('message'))
        continue

    issues = response.json()

    # Step 3: Edit the issues that have the same name as the issues in a directory
    issue_dir = 'issues'
    for issue in issues:
        issue_title = issue['title'] + '.md'
        issue_file_path = os.path.join(issue_dir, issue_title)
        
        if os.path.exists(issue_file_path):
            print(f"Found issue: {issue_title} in {repo_name}")
            with open(issue_file_path, 'r') as f:
                new_body = f.read()
            
            data = {
                'body': new_body
            }
            response = requests.patch(f'https://api.github.com/repos/insper-classroom/{repo_name}/issues/{issue["number"]}', headers=headers, json=data)
            
            if response.status_code == 200:
                print(f"Updated issue: {issue_title} in {repo_name}")
            else:
                print(f"Failed to update issue: {issue_title} in {repo_name}. Error: {response.json().get('message')}")

print("Done!")
