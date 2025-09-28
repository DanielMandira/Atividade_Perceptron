# MANUAL DE USO - SISTEMA PERCEPTRON PARA CLASSIFICAÇÃO DE FERRAMENTAS

## REQUISITOS DO SISTEMA

- Python 3.6 ou superior
- Sistema operacional: Windows, Linux ou macOS
- Arquivos necessários:
  - perceptron.py
  - dataset_ferramentas.csv
  - dataset_teste.csv

## COMO EXECUTAR

### 1. Preparação
```bash
# Navegue até o diretório do projeto
cd caminho/para/perceptron

# Verifique se os arquivos estão presentes
ls -la  # (Linux/macOS) ou dir (Windows)
```

### 2. Execução
```bash
python perceptron.py
```

### 3. Saída Esperada

O programa irá:
1. Carregar o dataset de treinamento
2. Mostrar o vocabulário de funções criado
3. Treinar o Perceptron
4. Exibir os pesos aprendidos
5. Testar no dataset de teste
6. Mostrar a acurácia obtida
7. Abrir interface para classificação interativa

## EXEMPLO DE USO DA INTERFACE

```
Classificacao de Ferramentas
------------------------------
Nome: Chave Phillips
Peso (g): 180
Dureza (1-10): 7
Tamanho (cm): 17
Tem cabo (1/0): 1
Metal (1/0): 1
Funcao: Apertar parafusos Phillips

Chave Phillips:
-> FERRAMENTA

Continuar (s/n)? n
```

## INTERPRETAÇÃO DOS RESULTADOS

### Pesos das Características Físicas
- **Peso positivo alto:** Característica importante para identificar ferramentas
- **Peso negativo alto:** Característica importante para identificar não-ferramentas
- **Peso próximo de zero:** Característica pouco relevante

### Pesos das Características Textuais
- Palavras com peso positivo: Associadas a ferramentas
- Palavras com peso negativo: Associadas a não-ferramentas

### Acurácia
- **100%:** Classificação perfeita
- **≥ 80%:** Bom desempenho
- **< 70%:** Possível necessidade de mais dados ou características

## TROUBLESHOOTING

### Erro: "Arquivo não encontrado"
- Verifique se os arquivos CSV estão no mesmo diretório do script
- Verifique a codificação dos arquivos (UTF-8)

### Erro: "Invalid literal for float()"
- Verifique se os dados numéricos nos CSVs estão corretos
- Use ponto (.) como separador decimal, não vírgula (,)

### Baixa acurácia
- Verifique se os dados estão balanceados
- Considere adicionar mais amostras de treinamento
- Revise as características utilizadas

## MODIFICAÇÕES POSSÍVEIS

### Adicionar novas características
1. Edite a função `carregar_dataset()`
2. Ajuste os índices das colunas
3. Atualize a normalização se necessário

### Alterar parâmetros de treinamento
```python
modelo = Perceptron(taxa_aprendizado=0.05, max_iteracoes=2000)
```

### Modificar o vocabulário textual
Edite a função `extrair_palavras_chave_funcao()` para:
- Alterar o tamanho mínimo das palavras
- Adicionar/remover stopwords
- Incluir processamento adicional do texto
