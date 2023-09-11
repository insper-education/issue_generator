Definir e configurar pino que será usado para conectar o botão de seleção musical.

- [ ] Atualizar `README.md` com definição do pino.
- [ ] Inserir `#defines` no  `main.c` com valores certos

```c
#define SELECAO_PIO
#define SELECAO_PIO_ID
#define SELECAO_PIO_IDX
#define SELECAO_PIO_IDX_MASK
```

- [ ] Atualizar função  `init()` configurando o pino do botão como input

Dicas (opcional):

- [ ] Criar função `int get_selecao();` que retorna o status do botão (1/0)