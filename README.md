# Atividade Perceptron - Detecção de Ferramentas de Material de Construção

## 📋 Sobre o Projeto

Este repositório foi criado para a atividade acadêmica da disciplina de **Redes Neurais** da **FATEC de Registro**, com foco na implementação de um perceptron para detecção e classificação de ferramentas de material de construção.

## 🎯 Objetivo

O objetivo principal desta atividade é aplicar os conceitos teóricos de redes neurais artificiais, especificamente o modelo do perceptron, para resolver um problema prático de classificação de imagens de ferramentas utilizadas na construção civil.

## 🔧 Ferramentas a serem Detectadas

O sistema será treinado para identificar diferentes tipos de ferramentas de construção, tais como:
- Martelos
- Chaves de fenda
- Alicates
- Furadeiras
- Serras
- Níveis
- Trenas
- E outras ferramentas comuns na construção civil

## 🧠 Conceitos Aplicados

### Perceptron
O perceptron é o modelo mais simples de rede neural artificial, sendo a base para o entendimento de redes mais complexas. Neste projeto, utilizamos:

- **Função de ativação**: Para determinar se um neurônio deve ser ativado
- **Pesos sinápticos**: Para ajustar a importância de cada entrada
- **Algoritmo de aprendizado**: Para treinar o modelo com exemplos
- **Classificação binária/multiclasse**: Para categorizar as ferramentas

## 📚 Contexto Acadêmico

**Instituição**: FATEC de Registro (Faculdade de Tecnologia de Registro)  
**Disciplina**: Redes Neurais  
**Tipo**: Atividade Prática  
**Modelo**: Perceptron  

## 🚀 Como Utilizar

1. Clone este repositório:
```bash
git clone https://github.com/DanielMandira/Atividade_Perceptron.git
```

2. Navegue até o diretório do projeto:
```bash
cd Atividade_Perceptron
```

3. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

4. Execute o programa principal:
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
Atividade_Perceptron/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt      # Dependências do projeto
├── main.py              # Arquivo principal
├── perceptron.py        # Implementação do perceptron
├── data/                # Dataset com imagens das ferramentas
│   ├── training/        # Dados de treinamento
│   └── testing/         # Dados de teste
├── models/              # Modelos treinados
└── utils/               # Funções auxiliares
    ├── preprocessing.py # Pré-processamento de imagens
    └── visualization.py # Visualização de resultados
```

## 📊 Dataset

O dataset contém imagens de ferramentas de construção organizadas por categoria, permitindo o treinamento supervisionado do perceptron para classificação multiclasse.

## 🎓 Aprendizados Esperados

Ao completar esta atividade, espera-se que os alunos compreendam:

- Funcionamento básico de redes neurais
- Implementação prática do algoritmo perceptron
- Pré-processamento de dados para machine learning
- Avaliação de modelos de classificação
- Aplicação de IA em problemas reais

## 📈 Métricas de Avaliação

O desempenho do modelo será avaliado através de:
- Acurácia
- Precisão
- Recall
- F1-Score
- Matriz de confusão

## 🤝 Contribuições

Este é um projeto acadêmico desenvolvido como parte do curso de Redes Neurais. Contribuições e sugestões são bem-vindas para fins educacionais.

## 📝 Licença

Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).

## 👨‍🎓 Autor

Desenvolvido como atividade acadêmica para a disciplina de Redes Neurais na FATEC de Registro.

---

*Este projeto faz parte do currículo acadêmico e tem como objetivo principal o aprendizado prático dos conceitos de redes neurais artificiais.*