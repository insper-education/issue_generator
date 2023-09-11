# Issues Generator
O "Issues Generator" é um repositório template projetado para automatizar a criação de issues quando um aluno aceita uma tarefa via GitHub Classroom.

# Funcionamento
Este repositório utiliza uma automação para criar issues apenas quando o aluno aceita a atividade do gitclassroom. Os issues são baseados em arquivos .md presentes dentro do diretório `.github/issues`. Cada arquivo corresponde a um issue, e o nome do arquivo é usado como título do issue.

## Como os Issues são Criados
Quando um push é feito na branch main, uma GitHub Action é acionada. Esta Action verifica se há issues abertos no repositório. Se não houver issues abertos, a Action lê os arquivos .md do diretório especificado e cria um issue para cada arquivo, usando o conteúdo do arquivo como corpo do issue. Devido a limitacoes do trigger do github action, este metodo criara os issues novamente se o aluno fechar todos os issues em seu repositorio e dar um novo commit.

# Sobre o "insper_bot"
Os issues são criados em nome do usuário "insper_bot". Este bot possui uma chave de acesso (Personal Access Token) que lhe permite criar issues que esta disponiveis como um segredo da organizacao insper_classroom com o nome `ISSUE_GENERATOR`. Por razões de segurança, esta chave pertence exclusivamente ao "insper_bot" e não deve ser compartilhada ou exposta.

# Instalacao
Para utilizar essa automacao voce pode criar em fork deste reositorio ou copiar a pasta oculta `.github` para o template-repositorio que voce vai utilizar em sua atividade.

## Criando seus próprios Issues após o Fork
Modifique ou arquivos .md dentro do diretório `.github/issues`. Cada arquivo corresponde a um issue, e o nome do arquivo é usado como título do issue.

# Contribuindo
Se você encontrar erros ou quiser contribuir de alguma forma, siga o processo de fork, crie uma nova branch, faça suas alterações e, em seguida, abra um Pull Request.
