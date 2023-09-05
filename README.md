# Create Issue on First Push

## Instalation

Para criar um issues no repositorio eh nescessario criar um github secret com o nome **SECRET** e contendo uma chave PAT de um repositorio com direito a escrita.

## Funcionamento

Este action cria um issue nos repositorios dos alunos **APOS** o primeiro push.

A action consiste de dois estagios, *Check for open issues* conta o numero de issues **abertos** salvando em uma variavel booleana (True se existem open-issues). 

O ssegundo estagio cria um novo issue, customize modificando *title* e *body*.
