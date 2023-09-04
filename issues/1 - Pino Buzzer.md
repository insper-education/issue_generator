Definir e configurar pino que será usado para conectar o buzzer.

- [ ] Atualizar `README.md` com definição do pino.
- [ ] Inserir `#defines` no  `main.c` com valores certos
```c
#define BUZZER_PIO
#define BUZZER_PIO_ID
#define BUZZER_PIO_IDX
#define BUZZER_PIO_IDX_MASK
```
- [ ] Atualizar função  `init()` configurando o pino do buzzer como output

Dicas (opcional):

- [ ] Criar função `void set_buzzer();` que coloca 1 no pino do buzzer
- [ ] Criar função `void clear_buzzer();` que coloca 0 no pino do buzzer