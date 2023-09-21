import requests
import os

# Step 1: Get GitHub credentials from a file
with open('credentials.txt', 'r') as f:
    PAT = f.readline().strip()

headers = {
    'Authorization': f'token {PAT}',
    'Accept': 'application/vnd.github.v3+json'
}

# Step 2: Given a repo link, list all open issues
# repo_link = input("Enter the GitHub repo link (format: owner/repo): ")
repo_link = "insper-education/issue_generator"
response = requests.get(f'https://api.github.com/repos/{repo_link}/issues', headers=headers, params={'state': 'open'})

if response.status_code != 200:
    print("Error fetching issues:", response.json().get('message'))
    exit()

issues = response.json()

# Step 3: Edit the issues that have the same name as the issues in a directory
issue_dir = 'issues'
for issue in issues:
    issue_title = issue['title'] + '.md'
    issue_file_path = os.path.join(issue_dir, issue_title)
    
    if os.path.exists(issue_file_path):
        print(f"Found issue: {issue_title}")
        with open(issue_file_path, 'r') as f:
            new_body = f.read()
        
        data = {
            'body': new_body
        }
        
        response = requests.patch(f'https://api.github.com/repos/{repo_link}/issues/{issue["number"]}', headers=headers, json=data)
        
        if response.status_code == 200:
            print(f"Updated issue: {issue_title}")
        else:
            print(f"Failed to update issue: {issue_title}. Error: {response.json().get('message')}")

print("Done!")
