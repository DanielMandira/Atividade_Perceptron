# 📋 Exemplos de Uso do Sistema de Classificação de Ferramentas

## 🚀 Execução Básica

### Executar o sistema completo
```bash
python3 main.py
```

### Executar apenas o módulo perceptron
```bash
cd src
python3 perceptron_melhorado.py
```

## 🔧 Exemplos de Classificação Manual

Quando o sistema solicitar os dados dos itens, você pode usar estes exemplos:

### Exemplo 1: Ferramenta - Chave de Fenda
```
Nome do item: Chave de Fenda Pequena
Peso (gramas): 180
Dureza (1-10): 7
Tamanho (cm): 18
Tem cabo? (1=sim, 0=não): 1
Material metálico? (1=sim, 0=não): 1
Função/uso do item: Aparafusar parafusos pequenos
```
**Resultado Esperado:** FERRAMENTA ✅

### Exemplo 2: Ferramenta - Martelo
```
Nome do item: Martelo de Carpinteiro
Peso (gramas): 340
Dureza (1-10): 8
Tamanho (cm): 28
Tem cabo? (1=sim, 0=não): 1
Material metálico? (1=sim, 0=não): 1
Função/uso do item: Martelar pregos em madeira
```
**Resultado Esperado:** FERRAMENTA ✅

### Exemplo 3: Não-Ferramenta - Caderno
```
Nome do item: Caderno Escolar
Peso (gramas): 220
Dureza (1-10): 2
Tamanho (cm): 21
Tem cabo? (1=sim, 0=não): 0
Material metálico? (1=sim, 0=não): 0
Função/uso do item: Anotar aulas e fazer exercícios
```
**Resultado Esperado:** NÃO É FERRAMENTA ✅

### Exemplo 4: Não-Ferramenta - Borracha
```
Nome do item: Borracha Escolar
Peso (gramas): 45
Dureza (1-10): 3
Tamanho (cm): 6
Tem cabo? (1=sim, 0=não): 0
Material metálico? (1=sim, 0=não): 0
Função/uso do item: Apagar escritos à lápis
```
**Resultado Esperado:** NÃO É FERRAMENTA ✅

### Exemplo 5: Caso Limite - Régua de Metal
```
Nome do item: Régua de Metal
Peso (gramas): 150
Dureza (1-10): 6
Tamanho (cm): 30
Tem cabo? (1=sim, 0=não): 0
Material metálico? (1=sim, 0=não): 1
Função/uso do item: Medir e traçar linhas retas
```
**Resultado Esperado:** Pode variar (caso limite)

## 📊 Interpretação dos Resultados

### Características que indicam FERRAMENTA:
- **Peso moderado a alto** (200-800g)
- **Dureza alta** (6-10)
- **Presença de cabo** (1)
- **Material metálico** (1)
- **Função relacionada a:** construção, reparo, corte, fixação, impacto

### Características que indicam NÃO-FERRAMENTA:
- **Peso baixo** (< 200g)
- **Dureza baixa** (1-5)
- **Sem cabo** (0)
- **Sem metal ou metal mínimo** (0)
- **Função relacionada a:** escrita, leitura, educação, limpeza

## 🎯 Categorias de Função Reconhecidas

O sistema reconhece estas categorias principais de função:

1. **Martelar pregos e objetos** - Ferramentas de impacto
2. **Aparafusar e fixar componentes** - Ferramentas de fixação
3. **Cortar madeira e materiais** - Ferramentas de corte
4. **Perfurar buracos em materiais** - Ferramentas de perfuração
5. **Manipular e segurar objetos** - Ferramentas de manipulação
6. **Cavar e mover terra** - Ferramentas de movimento de solo
7. **Escrever e marcar** - Itens de escrita/medição
8. **Medir e alinhar objetos** - Instrumentos de medição
9. **Outros usos diversos** - Categoria geral

## 💡 Dicas para Melhores Resultados

1. **Seja preciso com o peso**: Use uma balança se possível
2. **Avalie a dureza corretamente**: 1=muito mole, 10=muito duro
3. **Meça o tamanho principal**: Comprimento, largura ou altura predominante
4. **Descreva a função claramente**: Use termos específicos da função principal
5. **Considere o contexto**: Pense se o item seria encontrado em uma loja de construção

## 🔄 Comandos do Sistema

Durante a execução, você pode usar:
- **'sair'** - Para encerrar a classificação manual
- **'s' ou 'sim'** - Para continuar classificando itens
- **'n' ou 'não'** - Para parar e encerrar o programa

## 📈 Métricas de Avaliação

O sistema exibirá:
- **Acurácia no treinamento**: Percentual de acertos no dataset de treino
- **Acurácia no teste**: Percentual de acertos no dataset de teste independente
- **Informações do modelo**: Detalhes sobre pesos, bias e vocabulário
- **Histórico de treinamento**: Convergência e iterações realizadas