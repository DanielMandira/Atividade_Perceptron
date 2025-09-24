# Exemplo de Execução do Sistema de Classificação de Ferramentas

## Como usar o sistema

1. Execute o programa:
```bash
python perceptron.py
```

2. Acompanhe o treinamento do modelo

3. Quando chegar na interface interativa, teste com os exemplos abaixo:

## Exemplos para Testar

### Exemplo 1 - Ferramenta Típica
```
Nome do item: Chave de Boca
Peso em gramas: 180
Dureza na escala 1-10: 8
Tamanho em cm: 16
Tem cabo? (1=Sim, 0=Não): 1
É feito de material metálico? (1=Sim, 0=Não): 1
Qual a função/uso do item?: Apertar e afrouxar porcas
```
**Resultado esperado**: FERRAMENTA (alta confiança)

### Exemplo 2 - Não-Ferramenta Típica
```
Nome do item: Caderno
Peso em gramas: 150
Dureza na escala 1-10: 2
Tamanho em cm: 21
Tem cabo? (1=Sim, 0=Não): 0
É feito de material metálico? (1=Sim, 0=Não): 0
Qual a função/uso do item?: Escrever e anotar
```
**Resultado esperado**: NÃO-FERRAMENTA (alta confiança)

### Exemplo 3 - Caso Ambíguo
```
Nome do item: Regua de Metal
Peso em gramas: 120
Dureza na escala 1-10: 6
Tamanho em cm: 30
Tem cabo? (1=Sim, 0=Não): 0
É feito de material metálico? (1=Sim, 0=Não): 1
Qual a função/uso do item?: Medir distancias
```
**Resultado esperado**: Análise mais complexa (confiança baixa/média)

### Exemplo 4 - Ferramenta Pesada
```
Nome do item: Britadeira
Peso em gramas: 950
Dureza na escala 1-10: 9
Tamanho em cm: 50
Tem cabo? (1=Sim, 0=Não): 1
É feito de material metálico? (1=Sim, 0=Não): 1
Qual a função/uso do item?: Quebrar concreto e asfalto
```
**Resultado esperado**: FERRAMENTA (alta confiança)

### Exemplo 5 - Item de Escritório
```
Nome do item: Grampeador
Peso em gramas: 200
Dureza na escala 1-10: 4
Tamanho em cm: 15
Tem cabo? (1=Sim, 0=Não): 0
É feito de material metálico? (1=Sim, 0=Não): 1
Qual a função/uso do item?: Grampear papeis
```
**Resultado esperado**: Análise interessante (pode variar)

## O que o Sistema Analisa

### Características Físicas (Perceptron):
- Peso, dureza, tamanho
- Presença de cabo
- Material metálico

### Análise de Função:
- Palavras-chave que indicam uso como ferramenta
- Palavras-chave que indicam uso não-ferramenta
- Contexto da função descrita

### Decisão Final:
- Combina ambas as análises
- Fornece nível de confiança
- Explica o raciocínio

## Interpretação dos Resultados

- **✅ Alta Confiança**: Perceptron e análise de função concordam
- **⚠️ Baixa Confiança**: Perceptron e análise de função discordam
- **❓ Média Confiança**: Análise de função inconclusiva
- **🔍 Análise da Função**: Mostra se a função é típica de ferramenta
- **🤖 Perceptron**: Resultado baseado apenas nas características físicas
