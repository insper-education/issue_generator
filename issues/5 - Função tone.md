Criar função `tone` que gera um tom no pino do buzzer. Para
mais informações acesse:

- https://insper.github.io/ComputacaoEmbarcada/APS-1-Musical-software/#tone

Para validar execute algumas notas por tempos diferentes.

```c
for (int freq=200; freq<5000; freq+=500){
tone(freq, 200 + freq/2);
delay_ms(200);
}
```
