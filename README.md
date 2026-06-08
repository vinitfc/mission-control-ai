# Mission Control AI

## Missão: Nova Horizon
## Equipe: Cosmic Mavericks

## Integrantes

| Nome | RM |
|------|-----|
| Gabriel Jurado Nogueira | 571236 |
| Vinicius Torralles Ferreira Conduta | 570911 |
| Mariana Carminato | 573258 |

## Descrição do Projeto

O *Mission Control AI* é um sistema em Python que simula o monitoramento inteligente de uma missão espacial experimental. O programa analisa dados simulados da missão, gera alertas automáticos, calcula níveis de risco e apresenta um relatório final completo.

## Funcionalidades

- Armazenamento de dados da missão em matriz
- Análise de 6+ ciclos de monitoramento
- Classificação individual por métrica (NORMAL / ATENÇÃO / CRÍTICO)
- Pontuação de risco por ciclo (0 a 10 pontos)
- Classificação do ciclo (ESTÁVEL / ATENÇÃO / CRÍTICA)
- Identificação da tendência da missão (melhora/piora/estável)
- Identificação da área mais afetada
- Recomendações automáticas
- Relatório final completo no terminal

## Áreas Monitoradas

| Coluna | Área |
|--------|------|
| 0 | Temperatura interna |
| 1 | Comunicação com a base |
| 2 | Sistema de energia |
| 3 | Suporte de oxigênio |
| 4 | Estabilidade operacional |

## Regras de Alerta

### Temperatura
- NORMAL: 18°C a 30°C
- ATENÇÃO: menor que 18°C ou 30°C a 35°C
- CRÍTICO: maior que 35°C

### Comunicação
- NORMAL: 60% ou mais
- ATENÇÃO: 30% a 59%
- CRÍTICO: menor que 30%

### Bateria
- NORMAL: 50% ou mais
- ATENÇÃO: 20% a 49%
- CRÍTICO: menor que 20%

### Oxigênio
- NORMAL: 90% ou mais
- ATENÇÃO: 80% a 89%
- CRÍTICO: menor que 80%

### Estabilidade
- NORMAL: 70% ou mais
- ATENÇÃO: 40% a 69%
- CRÍTICO: menor que 40%

## Pontuação de Risco

| Classificação | Pontos |
|---------------|--------|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

*Máxima por ciclo: 10 pontos*

## Classificação do Ciclo

| Pontuação | Classificação |
|-----------|---------------|
| 0 a 2 | MISSÃO ESTÁVEL |
| 3 a 5 | MISSÃO EM ATENÇÃO |
| 6 a 10 | MISSÃO CRÍTICA |
