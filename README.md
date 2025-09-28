# 🔧 Sistema de Classificação de Ferramentas - Perceptron

> Sistema inteligente para identificação automática de ferramentas em loja de material de construção usando algoritmo Perceptron.

## 📋 Descrição

Este sistema implementa um classificador baseado em Perceptron para identificar automaticamente se um item é uma ferramenta ou não em uma loja de material de construção. O sistema analisa características físicas e funcionais para fazer a classificação com alta precisão.

## 🗂️ Estrutura do Projeto

```
Atividade_Perceptron/
├── main.py                         # Arquivo principal para executar o sistema
├── README.md                       # Documentação do projeto
├── LICENSE                         # Licença
├── requirements.txt                # Dependências Python
├── src/
│   └── classificador_ferramentas.py   # Implementação do classificador
├── data/
│   ├── dataset_ferramentas.csv        # Dataset de treinamento (30 registros)
│   ├── dataset_teste.csv              # Dataset de teste (10 registros)
│   └── legenda_funcoes.csv            # Legenda das categorias funcionais
└── docs/
    ├── MANUAL_USO.md                   # Manual de uso detalhado
    └── exemplos_uso.md                 # Exemplos práticos
```

## 🚀 Como Usar

### Instalação
```bash
pip install -r requirements.txt
```

### Execução
```bash
python3 main.py
```

## 📊 Características Analisadas

O sistema analisa as seguintes características dos itens:

### Características Físicas (5):
- **Peso** (gramas): Normalizado entre 7-800g
- **Dureza** (escala 1-10): Resistência do material
- **Tamanho** (cm): Dimensão principal
- **Tem cabo** (0/1): Presença de cabo ou punho
- **Material metálico** (0/1): Se contém metal

### Características Funcionais (9):
- **Código de função** (1-9): Categoria funcional usando one-hot encoding

## 🎯 Categorias de Função

| Código | Categoria | Descrição |
|--------|-----------|-----------|
| 1 | Impacto | Martelar pregos e objetos |
| 2 | Fixação | Aparafusar e fixar componentes |
| 3 | Corte | Cortar madeira e materiais |
| 4 | Perfuração | Perfurar buracos em materiais |
| 5 | Manipulação | Manipular e segurar objetos |
| 6 | Movimento de Solo | Cavar e mover terra |
| 7 | Escrita e Leitura | Escrever e marcar |
| 8 | Medição e Fixação | Medir e alinhar objetos |
| 9 | Outros | Outros usos diversos |

## 📈 Performance

- **Acurácia de Treinamento**: 100%
- **Acurácia de Teste**: 100%
- **Convergência**: ~3 iterações
- **Total de Características**: 14 (5 físicas + 9 funcionais)
- **Tempo de Execução**: <2 segundos

## 🔧 Funcionalidades

### Treinamento Automático
- Carregamento e processamento automático dos datasets
- Normalização das características físicas
- One-hot encoding das categorias funcionais
- Convergência rápida com alta precisão

### Interface Interativa
- Classificação manual de novos itens
- Validação de entrada de dados
- Feedback detalhado dos resultados
- Exibição da categoria funcional

### Análise do Modelo
- Visualização dos pesos aprendidos
- Histórico de treinamento
- Métricas de performance detalhadas
- Avaliação em dataset independente

## 📋 Requisitos

- Python 3.6+
- pandas
- openpyxl (opcional)

## 📚 Documentação

Consulte a pasta `docs/` para documentação adicional:
- **MANUAL_USO.md**: Manual detalhado de uso
- **exemplos_uso.md**: Exemplos práticos de classificação

## 📄 Licença

Este projeto está licenciado sob os termos especificados no arquivo LICENSE.