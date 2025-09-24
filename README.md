# Sistema de Classificação de Ferramentas com Perceptron

## Descrição do Projeto

Este projeto implementa um sistema de classificação binária usando o algoritmo Perceptron para identificar se um item é uma ferramenta ou não, baseado em suas características físicas e funcionais. A implementação é feita completamente do zero, sem uso de bibliotecas de machine learning externas.

## Características do Dataset

O dataset contém informações sobre diversos itens, incluindo ferramentas e objetos não-ferramentas, com os seguintes atributos:

### Atributos de Entrada (Features):
1. **peso_gramas**: Peso do item em gramas (numérico)
2. **dureza_escala_1_10**: Dureza do material na escala de 1 a 10 (numérico)
3. **tamanho_cm**: Tamanho do item em centímetros (numérico)
4. **tem_cabo**: Se o item possui cabo (binário: 1=Sim, 0=Não)
5. **material_metalico**: Se o item é feito de material metálico (binário: 1=Sim, 0=Não)

### Atributos Informativos:
- **nome_item**: Nome descritivo do item
- **preco_reais**: Preço do item em reais
- **funcao**: Descrição da função/uso do item

### Atributo Alvo:
- **eh_ferramenta**: Classificação binária (1=Ferramenta, 0=Não-ferramenta)

## Estrutura dos Arquivos

```
perceptron/
├── dataset_ferramentas.csv    # Dataset de treinamento (30 amostras)
├── dataset_teste.csv          # Dataset de teste (10 amostras)
├── perceptron.py              # Implementação principal do Perceptron
└── README.md                  # Este arquivo de documentação
```

## Exemplos do Dataset

### Ferramentas (eh_ferramenta = 1):
- Martelo: 250g, dureza 8, 25cm, tem cabo, metálico
- Chave de Fenda: 150g, dureza 6, 15cm, tem cabo, metálico
- Machado: 500g, dureza 9, 35cm, tem cabo, metálico

### Não-Ferramentas (eh_ferramenta = 0):
- Borracha: 50g, dureza 2, 8cm, sem cabo, não-metálico
- Papel: 80g, dureza 1, 5cm, sem cabo, não-metálico
- Livro: 200g, dureza 2, 15cm, sem cabo, não-metálico

## Implementação do Perceptron

### Características da Implementação:
- **Algoritmo**: Perceptron simples com função de ativação degrau
- **Taxa de Aprendizado**: 0.1 (configurável)
- **Função de Ativação**: Degrau unitário (step function)
- **Normalização**: Dados normalizados para intervalo [0,1]
- **Critério de Parada**: Convergência (zero erros) ou máximo de iterações

### Fórmulas Utilizadas:

1. **Saída Linear**: 
   ```
   y = w₁x₁ + w₂x₂ + w₃x₃ + w₄x₄ + w₅x₅ + bias
   ```

2. **Função de Ativação**:
   ```
   f(y) = 1 se y ≥ 0, caso contrário 0
   ```

3. **Regra de Atualização dos Pesos**:
   ```
   wᵢ = wᵢ + α × erro × xᵢ
   bias = bias + α × erro
   ```
   Onde α é a taxa de aprendizado e erro = (valor_real - predição)

## Como Executar

### Pré-requisitos:
- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (apenas bibliotecas padrão)

### Execução:
```bash
python perceptron.py
```

### Funcionalidades:
1. **Carregamento automático dos datasets**
2. **Treinamento do modelo** com visualização do progresso
3. **Teste automático** com cálculo de acurácia
4. **Interface interativa** para classificação de novos itens

## Exemplo de Uso Interativo

```
Digite as características do item para classificação:

Insira as características do item:
Peso em gramas (ex: 250): 300
Dureza na escala 1-10 (ex: 8): 7
Tamanho em cm (ex: 25): 20
Tem cabo? (1=Sim, 0=Não): 1
É feito de material metálico? (1=Sim, 0=Não): 1

----------------------------------------
RESULTADO: É uma FERRAMENTA! 🔧
----------------------------------------
```

## Resultados Esperados

Com o dataset fornecido, o Perceptron deve atingir:
- **Acurácia de Treinamento**: ~100% (dados linearmente separáveis)
- **Acurácia de Teste**: 90-100%
- **Convergência**: Normalmente em 50-200 iterações

## Análise dos Resultados

### Métricas de Avaliação:
- Acurácia no conjunto de treinamento
- Acurácia no conjunto de teste
- Número de iterações até convergência
- Análise dos pesos finais

### Interpretação dos Pesos:
- Pesos positivos altos indicam características que favorecem a classificação como ferramenta
- Pesos negativos indicam características que desfavorecem
- Magnitude dos pesos indica a importância da característica

## Limitações do Modelo

1. **Linearidade**: O Perceptron só pode separar dados linearmente separáveis
2. **Binário**: Apenas classificação binária (ferramenta vs não-ferramenta)
3. **Sensibilidade**: Sensível à escala dos dados (necessita normalização)
4. **Simplicidade**: Modelo simples, pode não capturar relações complexas

## Possíveis Melhorias

1. **Multi-classe**: Extensão para múltiplas categorias de ferramentas
2. **Validação Cruzada**: Implementar k-fold cross-validation
3. **Regularização**: Adicionar termos de regularização
4. **Interface Gráfica**: Desenvolver GUI para melhor usabilidade
5. **Mais Features**: Adicionar características como cor, marca, etc.

## Estrutura do Código

### Classes Principais:
- `Perceptron`: Implementação do algoritmo de aprendizado
- Funções auxiliares para carregamento, normalização e interface

### Métodos da Classe Perceptron:
- `treinar(X, y)`: Treina o modelo com dados fornecidos
- `prever(X)`: Faz previsões para novas amostras
- `calcular_acuracia(X, y)`: Calcula acurácia do modelo

## Considerações Técnicas

### Normalização:
Os dados são normalizados para o intervalo [0,1] usando min-max scaling:
```
valor_normalizado = (valor - min) / (max - min)
```

### Inicialização:
Pesos e bias são inicializados com valores aleatórios pequenos (-0.1 a 0.1) para evitar simetria e garantir aprendizado.

## Aplicações Práticas

Este sistema pode ser aplicado em:
- **Controle de Estoque**: Classificação automática de itens em lojas
- **E-commerce**: Categorização de produtos
- **Inventário Industrial**: Organização de equipamentos
- **Educação**: Demonstração de conceitos de machine learning

## Conclusão

O projeto demonstra uma implementação completa e educativa do algoritmo Perceptron, mostrando como um modelo simples de machine learning pode resolver problemas de classificação binária de forma efetiva. A implementação sem bibliotecas externas permite compreender completamente o funcionamento interno do algoritmo.
