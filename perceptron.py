import csv
import random

class Perceptron:
    def __init__(self, taxa_aprendizado=0.01, max_iteracoes=1000):
        self.taxa_aprendizado = taxa_aprendizado
        self.max_iteracoes = max_iteracoes
        self.pesos = None
        self.bias = None
        self.historico_treinamento = []
    
    def _funcao_ativacao(self, x):
        return 1 if x >= 0 else 0
    
    def _produto_escalar(self, lista1, lista2):
        resultado = 0
        for i in range(len(lista1)):
            resultado += lista1[i] * lista2[i]
        return resultado
    
    def treinar(self, X, y):
        n_amostras = len(X)
        n_caracteristicas = len(X[0])
        
        self.pesos = [random.uniform(-0.1, 0.1) for _ in range(n_caracteristicas)]
        self.bias = random.uniform(-0.1, 0.1)
        
        for iteracao in range(self.max_iteracoes):
            erros = 0
            
            for i in range(n_amostras):
                saida_linear = self._produto_escalar(X[i], self.pesos) + self.bias
                predicao = self._funcao_ativacao(saida_linear)
                erro = y[i] - predicao
                
                if erro != 0:
                    erros += 1
                    for j in range(n_caracteristicas):
                        self.pesos[j] += self.taxa_aprendizado * erro * X[i][j]
                    self.bias += self.taxa_aprendizado * erro
            
            if erros == 0:
                break
    
    def prever(self, X):
        if isinstance(X[0], (int, float)):
            saida_linear = self._produto_escalar(X, self.pesos) + self.bias
            return self._funcao_ativacao(saida_linear)
        else:
            previsoes = []
            for amostra in X:
                saida_linear = self._produto_escalar(amostra, self.pesos) + self.bias
                previsoes.append(self._funcao_ativacao(saida_linear))
            return previsoes
    
    def calcular_acuracia(self, X, y):
        previsoes = self.prever(X)
        corretas = sum(1 for i in range(len(y)) if previsoes[i] == y[i])
        return (corretas / len(y)) * 100
    
    def mostrar_pesos(self, nomes_caracteristicas=None):
        print("\nPesos aprendidos:")
        if nomes_caracteristicas is None:
            nomes_caracteristicas = ["Peso", "Dureza", "Tamanho", "Tem_cabo", "Metal"]
        
        for i, caracteristica in enumerate(nomes_caracteristicas):
            print(f"{caracteristica}: {self.pesos[i]:.3f}")
        print(f"Bias: {self.bias:.3f}")


def extrair_palavras_chave_funcao(funcoes):
    """Extrai palavras-chave das funções e cria vocabulário"""
    palavras_importantes = set()
    
    # Processa todas as funções para encontrar palavras-chave
    for funcao in funcoes:
        palavras = funcao.lower().replace(',', ' ').replace('.', ' ').split()
        for palavra in palavras:
            if len(palavra) >= 3:  # Palavras com pelo menos 3 caracteres
                palavras_importantes.add(palavra)
    
    # Filtra palavras muito comuns e mantém as mais relevantes
    palavras_filtradas = []
    for palavra in sorted(palavras_importantes):
        if palavra not in ['para', 'com', 'por', 'das', 'dos', 'uma', 'uns', 'que', 'são', 'ter']:
            palavras_filtradas.append(palavra)
    
    return palavras_filtradas

def processar_funcao_para_features(funcao, vocabulario):
    """Converte uma função em vetor binário baseado no vocabulário"""
    funcao_lower = funcao.lower()
    features = []
    
    for palavra in vocabulario:
        if palavra in funcao_lower:
            features.append(1)
        else:
            features.append(0)
    
    return features

def carregar_dataset(nome_arquivo, vocabulario_funcao=None):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            cabecalho = next(leitor)
            
            dados = []
            rotulos = []
            nomes_itens = []
            funcoes = []
            
            # Primeira passada para coletar todas as funções
            linhas = list(leitor)
            for linha in linhas:
                if linha:
                    funcoes.append(linha[7])  # Coluna 'funcao'
            
            # Se vocabulário não foi fornecido, cria um novo
            if vocabulario_funcao is None:
                vocabulario_funcao = extrair_palavras_chave_funcao(funcoes)
            
            # Segunda passada para processar os dados
            for linha in linhas:
                if linha:
                    nomes_itens.append(linha[0])
                    
                    # Características físicas (colunas 1-5)
                    caracteristicas = [float(valor) for valor in linha[1:6]]
                    
                    # Adiciona características da função
                    funcao_features = processar_funcao_para_features(linha[7], vocabulario_funcao)
                    caracteristicas.extend(funcao_features)
                    
                    dados.append(caracteristicas)
                    rotulos.append(int(linha[-1]))
            
            return dados, rotulos, cabecalho, nomes_itens, vocabulario_funcao
    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' nao encontrado.")
        return None, None, None, None, None

def normalizar_dados(dados):
    if not dados:
        return dados
    
    n_caracteristicas = len(dados[0])
    dados_normalizados = []
    
    mins = [float('inf')] * n_caracteristicas
    maxs = [float('-inf')] * n_caracteristicas
    
    for amostra in dados:
        for i in range(n_caracteristicas):
            mins[i] = min(mins[i], amostra[i])
            maxs[i] = max(maxs[i], amostra[i])
    
    for amostra in dados:
        amostra_normalizada = []
        for i in range(n_caracteristicas):
            if maxs[i] - mins[i] != 0:
                valor_normalizado = (amostra[i] - mins[i]) / (maxs[i] - mins[i])
            else:
                valor_normalizado = 0
            amostra_normalizada.append(valor_normalizado)
        dados_normalizados.append(amostra_normalizada)
    
    return dados_normalizados

def interface_usuario(modelo, vocabulario_funcao):
    print("\nClassificacao de Ferramentas")
    print("-" * 30)
    
    while True:
        try:
            nome_item = input("Nome: ")
            peso = float(input("Peso (g): "))
            dureza = float(input("Dureza (1-10): "))
            tamanho = float(input("Tamanho (cm): "))
            tem_cabo = int(input("Tem cabo (1/0): "))
            material_metalico = int(input("Metal (1/0): "))
            funcao = input("Funcao: ")
            
            # Normalização das características físicas
            peso_norm = max(0, min(1, (peso - 60) / (800 - 60)))
            dureza_norm = max(0, min(1, (dureza - 1) / (9 - 1)))
            tamanho_norm = max(0, min(1, (tamanho - 4) / (45 - 4)))
            
            # Características físicas
            entrada = [peso_norm, dureza_norm, tamanho_norm, tem_cabo, material_metalico]
            
            # Adiciona características da função
            funcao_features = processar_funcao_para_features(funcao, vocabulario_funcao)
            entrada.extend(funcao_features)
            
            predicao = modelo.prever(entrada)
            
            print(f"\n{nome_item}:")
            if predicao == 1:
                print("-> FERRAMENTA")
            else:
                print("-> NAO E FERRAMENTA")
            
            if input("\nContinuar (s/n)? ").lower() != 's':
                break
                
        except ValueError:
            print("Erro nos valores digitados")
        except KeyboardInterrupt:
            break

def main():
    print("Perceptron - Classificacao de Ferramentas")
    
    # Carrega dataset de treinamento e cria vocabulário
    resultado_treino = carregar_dataset('dataset_ferramentas.csv')
    if resultado_treino[0] is None:
        return
    
    X_treino, y_treino, cabecalho, nomes_treino, vocabulario_funcao = resultado_treino
    
    print(f"\nVocabulario de funcoes criado com {len(vocabulario_funcao)} palavras:")
    print(vocabulario_funcao[:10], "..." if len(vocabulario_funcao) > 10 else "")
    
    X_treino_norm = normalizar_dados(X_treino)
    
    # Cria nomes das características
    nomes_caracteristicas = ["Peso", "Dureza", "Tamanho", "Tem_cabo", "Metal"]
    nomes_caracteristicas.extend([f"palavra_{palavra}" for palavra in vocabulario_funcao])
    
    modelo = Perceptron(taxa_aprendizado=0.1, max_iteracoes=1000)
    modelo.treinar(X_treino_norm, y_treino)
    modelo.mostrar_pesos(nomes_caracteristicas)
    
    # Testa no dataset de teste usando o mesmo vocabulário
    resultado_teste = carregar_dataset('dataset_teste.csv', vocabulario_funcao)
    if resultado_teste[0] is not None:
        X_teste, y_teste, _, nomes_teste, _ = resultado_teste
        X_teste_norm = normalizar_dados(X_teste)
        acuracia = modelo.calcular_acuracia(X_teste_norm, y_teste)
        print(f"\nAcuracia no dataset de teste: {acuracia:.1f}%")
    
    interface_usuario(modelo, vocabulario_funcao)

if __name__ == "__main__":
    main()
