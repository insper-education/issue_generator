# Issues Generator

O "Issues Generator" é um repositório template projetado para automatizar a criação de issues quando um aluno aceita uma tarefa via GitHub Classroom.

## Funcionamento

O processo é simples e eficiente:

1. **Arquivos .md**: Os issues são baseados em arquivos `.md` localizados no diretório `.github/issues`. Cada arquivo representa um issue, sendo que o nome do arquivo define o título do issue criado.

2. **Trigger do GitHub Action**: Ao realizar um push na branch `main`, uma GitHub Action é ativada. Esta verifica se já existem issues abertos no repositório. Caso não haja, ela lê os arquivos `.md` do diretório mencionado e cria um issue para cada um. Vale ressaltar que, devido às limitações do trigger da GitHub Action, se o aluno fechar todos os issues e realizar um novo commit, os issues serão recriados.

## Sobre o "insper_bot"

A criação dos issues é feita em nome do usuário "insper_bot". Este bot tem uma chave de acesso (Personal Access Token) que permite a criação de issues. Esta chave está armazenada como um segredo da organização `insper_classroom` sob o nome `ISSUE_GENERATOR`. Por razões de segurança, a chave é de uso exclusivo do "insper_bot" e não deve ser compartilhada ou exposta.

## Instalação

Para aproveitar essa automação:

1. **Fork**: Você pode simplesmente fazer um fork deste repositório.
   
2. **Cópia**: Alternativamente, copie a pasta oculta `.github` e adicione-a ao repositório template que você pretende usar em sua atividade.

### Personalizando os Issues

Para criar seus próprios issues, basta modificar ou adicionar arquivos `.md` dentro do diretório `.github/issues`. Lembre-se: o nome do arquivo define o título do issue.

## Contribuição

Contribuições são sempre bem-vindas! Se você identificar erros ou desejar adicionar melhorias:

1. Faça um fork deste repositório.
2. Crie uma nova branch.
3. Realize suas alterações.
4. Abra um Pull Request para integrar suas mudanças.
