# RELATÓRIO TÉCNICO: SISTEMA DE CLASSIFICAÇÃO DE FERRAMENTAS USANDO PERCEPTRON

**Disciplina:** Inteligência Artificial  
**Curso:** Desenvolvimento de Software Multiplataforma  
**Instituição:** FATEC  
**Data:** 17 de setembro de 2025  

---

## 1. INTRODUÇÃO

### 1.1 Contextualização do Problema

A classificação automatizada de objetos é um problema fundamental em inteligência artificial e aprendizado de máquina. No contexto industrial e comercial, a capacidade de identificar automaticamente se um item é uma ferramenta ou não pode ser aplicada em sistemas de inventário, controle de qualidade, segurança no trabalho e organização de almoxarifados.

### 1.2 Objetivo

Este trabalho apresenta o desenvolvimento de um sistema de classificação binária baseado no algoritmo Perceptron, implementado em Python puro (sem bibliotecas externas), capaz de identificar se um item é uma ferramenta ou não, considerando tanto características físicas quanto informações textuais sobre a função do objeto.

### 1.3 Justificativa

O Perceptron, proposto por Frank Rosenblatt em 1958, é um dos algoritmos mais fundamentais do aprendizado de máquina. Sua implementação do zero permite compreender os conceitos básicos de redes neurais artificiais, função de ativação, aprendizado supervisionado e otimização de pesos.

---

## 2. DESCRIÇÃO DO MODELO

### 2.1 Arquitetura do Perceptron

O modelo implementado segue a arquitetura clássica do Perceptron:

- **Entrada:** Vetor de características X = [x₁, x₂, ..., xₙ]
- **Pesos:** Vetor W = [w₁, w₂, ..., wₙ]
- **Bias:** Valor escalar b
- **Função de Ativação:** Função degrau (step function)
- **Saída:** Classificação binária (0 ou 1)

### 2.2 Função de Ativação

```
f(x) = {
  1, se x ≥ 0
  0, se x < 0
}
```

Onde x = W·X + b (produto escalar dos pesos com as características mais o bias)

### 2.3 Taxa de Aprendizado

- **Valor utilizado:** 0.1
- **Máximo de iterações:** 1000
- **Critério de parada:** Convergência (erro = 0)

### 2.4 Algoritmo de Treinamento

1. Inicialização aleatória dos pesos e bias (valores entre -0.1 e 0.1)
2. Para cada época:
   - Para cada amostra de treinamento:
     - Calcular saída linear: y = W·X + b
     - Aplicar função de ativação: ŷ = f(y)
     - Calcular erro: e = y_real - ŷ
     - Atualizar pesos: wᵢ = wᵢ + α × e × xᵢ
     - Atualizar bias: b = b + α × e
3. Parar quando erro = 0 ou máximo de iterações atingido

---

## 3. BASE DE DADOS UTILIZADA

### 3.1 Estrutura do Dataset

Os datasets contêm 8 colunas com as seguintes características:

| Coluna | Descrição | Tipo | Faixa de Valores |
|--------|-----------|------|------------------|
| nome_item | Nome do objeto | String | Variável |
| peso_gramas | Peso em gramas | Numérico | 50-800g |
| dureza_escala_1_10 | Dureza em escala 1-10 | Numérico | 1-10 |
| tamanho_cm | Tamanho em centímetros | Numérico | 4-45cm |
| tem_cabo | Presença de cabo | Binário | 0 ou 1 |
| material_metalico | Material metálico | Binário | 0 ou 1 |
| preco_reais | Preço em reais | Numérico | Variável |
| funcao | Descrição da função | String | Variável |
| eh_ferramenta | Rótulo de classificação | Binário | 0 ou 1 |

### 3.2 Dataset de Treinamento

**Total de amostras:** 30
- **Ferramentas (classe 1):** 20 amostras
- **Não-ferramentas (classe 0):** 10 amostras

**Exemplos de ferramentas:**
- Martelo (250g, dureza 8, 25cm, com cabo, metálico)
- Chave de Fenda (150g, dureza 6, 15cm, com cabo, metálico)
- Machado (500g, dureza 9, 35cm, com cabo, metálico)

**Exemplos de não-ferramentas:**
- Borracha (50g, dureza 2, 8cm, sem cabo, não-metálico)
- Papel (80g, dureza 1, 5cm, sem cabo, não-metálico)
- Livro (200g, dureza 2, 15cm, sem cabo, não-metálico)

### 3.3 Dataset de Teste

**Total de amostras:** 10
- **Ferramentas (classe 1):** 5 amostras
- **Não-ferramentas (classe 0):** 5 amostras

### 3.4 Processamento das Características Textuais

Para incluir informações textuais da função, foi implementado um sistema de bag-of-words:

1. **Extração de vocabulário:** Coleta todas as palavras únicas das funções (≥3 caracteres)
2. **Filtragem:** Remove palavras muito comuns (stopwords)
3. **Codificação binária:** Cada palavra do vocabulário torna-se uma feature binária
4. **Integração:** As features textuais são concatenadas às características físicas

**Exemplo de processamento:**
- Função: "Bater e pregar"
- Vocabulário: ["bater", "pregar", "apertar", "cortar", ...]
- Feature vector: [1, 1, 0, 0, ...] (bater=1, pregar=1, outras=0)

---

## 4. PROCESSO DE TREINAMENTO E RESULTADOS

### 4.1 Normalização dos Dados

As características numéricas foram normalizadas usando min-max scaling:

```
x_norm = (x - x_min) / (x_max - x_min)
```

**Faixas de normalização:**
- Peso: 60-800g
- Dureza: 1-9
- Tamanho: 4-45cm
- Características binárias: mantidas como 0 ou 1

### 4.2 Características Finais do Modelo

**Total de características por amostra:**
- 5 características físicas normalizadas
- N características textuais binárias (onde N = tamanho do vocabulário)
- Total: 5 + N características

### 4.3 Resultados Esperados

**Métricas de avaliação:**
- Acurácia no dataset de treinamento
- Acurácia no dataset de teste
- Análise dos pesos aprendidos

**Pesos esperados (características físicas):**
- Peso: Peso positivo para ferramentas (ferramentas tendem a ser mais pesadas)
- Dureza: Peso positivo (ferramentas tendem a ser mais duras)
- Tamanho: Peso variável (ferramentas podem ter tamanhos diversos)
- Tem_cabo: Peso fortemente positivo (maioria das ferramentas tem cabo)
- Material_metálico: Peso positivo (ferramentas frequentemente são metálicas)

---

## 5. DISCUSSÃO CRÍTICA

### 5.1 Vantagens do Modelo

1. **Simplicidade:** Implementação direta e interpretável
2. **Eficiência:** Treinamento rápido com baixo custo computacional
3. **Interpretabilidade:** Pesos podem ser analisados para entender a importância das características
4. **Robustez:** Funciona bem com características linearmente separáveis
5. **Inclusão de texto:** Capacidade de processar informações textuais simples

### 5.2 Limitações

1. **Linearidade:** Apenas problemas linearmente separáveis podem ser resolvidos
2. **Sensibilidade a outliers:** Amostras atípicas podem afetar significativamente o treinamento
3. **Bag-of-words simples:** Processamento textual básico, sem contexto semântico
4. **Dataset pequeno:** Base de dados limitada pode não representar toda a variabilidade real
5. **Características manuais:** Dependência de engenharia manual de características

### 5.3 Possíveis Melhorias

1. **Aumento do dataset:** Incluir mais amostras e maior variedade de objetos
2. **Características adicionais:** Forma, cor, textura, densidade
3. **Processamento textual avançado:** TF-IDF, embeddings, análise semântica
4. **Validação cruzada:** Técnicas mais robustas de avaliação
5. **Ensemble methods:** Combinação com outros algoritmos
6. **Regularização:** Técnicas para evitar overfitting

### 5.4 Aplicações Práticas

1. **Sistemas de inventário automatizado**
2. **Controle de qualidade em linhas de produção**
3. **Organização automática de almoxarifados**
4. **Sistemas de segurança no trabalho**
5. **E-commerce:** Categorização automática de produtos**

---

## 6. CONCLUSÃO

O sistema de classificação de ferramentas baseado em Perceptron demonstrou ser uma solução viável para o problema proposto. A implementação em Python puro permitiu compreender os fundamentos do algoritmo e sua aplicação prática.

### 6.1 Principais Contribuições

1. **Implementação educacional:** Código claro e bem documentado do Perceptron
2. **Processamento multimodal:** Integração de características físicas e textuais
3. **Sistema completo:** Interface de usuário para classificação interativa
4. **Base experimental:** Dataset estruturado para experimentação

### 6.2 Resultados Alcançados

- Desenvolvimento de um classificador funcional
- Integração bem-sucedida de características físicas e textuais
- Interface amigável para teste do modelo
- Documentação completa do processo

### 6.3 Trabalhos Futuros

1. Implementação de redes neurais multicamadas (MLP)
2. Comparação com outros algoritmos de classificação
3. Expansão para classificação multiclasse
4. Desenvolvimento de interface gráfica
5. Deploy como aplicação web

### 6.4 Considerações Finais

Este trabalho demonstra a aplicabilidade dos conceitos fundamentais de aprendizado de máquina em problemas reais, servindo como base sólida para estudos mais avançados em inteligência artificial e redes neurais.

---

## REFERÊNCIAS

1. ROSENBLATT, F. The perceptron: a probabilistic model for information storage and organization in the brain. Psychological Review, v. 65, n. 6, p. 386-408, 1958.

2. MITCHELL, T. M. Machine Learning. McGraw-Hill, 1997.

3. HAYKIN, S. Neural Networks and Learning Machines. 3rd ed. Pearson, 2008.

4. RUSSELL, S.; NORVIG, P. Artificial Intelligence: A Modern Approach. 4th ed. Pearson, 2020.

5. GÉRON, A. Hands-On Machine Learning with Scikit-Learn and TensorFlow. O'Reilly Media, 2017.

---

**Anexos:**
- Código fonte completo (perceptron.py)
- Dataset de treinamento (dataset_ferramentas.csv)
- Dataset de teste (dataset_teste.csv)
- Manual de uso do sistema
