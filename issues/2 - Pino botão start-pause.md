Definir e configurar pino que será usado para conectar o botão de start/pause.

- [ ] Atualizar `README.md` com definição do pino.
- [ ] Inserir `#defines` no  `main.c` com valores certos

```c
#define START_PIO
#define START_PIO_ID
#define START_PIO_IDX
#define START_PIO_IDX_MASK
```
- [x] Atualizar função  `init()` configurando o pino do botão como input

Dicas (opcional):

- [ ] Criar função `int get_startstop();` que retorna o status do botão (1/0)