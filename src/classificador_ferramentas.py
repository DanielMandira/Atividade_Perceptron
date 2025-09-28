#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import random
import json
import datetime
from typing import List, Tuple, Optional


class PerceptronFerramentas:
    """    
    Attributes:
        taxa_aprendizado (float): Taxa de aprendizado do perceptron
        max_iteracoes (int): Número máximo de iterações de treinamento
        pesos (List[float]): Pesos das características aprendidos
        bias (float): Bias do perceptron
        hist    # Carrega dataset de treinamento
    dados_treino = carregar_dataset_csv('data/dataset_ferramentas.csv')
    if dados_treino is None:
        print("❌ Erro: Não foi possível carregar o dataset de treinamento.")
        return_treinamento (List[dict]): Histórico do processo de treinamento
        legenda_funcoes (dict): Mapeamento código -> descrição das funções
    """
    
    def __init__(self, taxa_aprendizado: float = 0.1, max_iteracoes: int = 1000):
        """
        Inicializa o perceptron com os parâmetros especificados.
        
        Args:
            taxa_aprendizado (float): Taxa de aprendizado (padrão: 0.1)
            max_iteracoes (int): Máximo de iterações (padrão: 1000)
        """
        self.taxa_aprendizado = taxa_aprendizado
        self.max_iteracoes = max_iteracoes
        self.pesos = None
        self.bias = None
        self.historico_treinamento = []
        
        # Parâmetros de normalização baseados no dataset
        self.normalizacao_params = {
            'peso': {'min': 7, 'max': 800},      # Atualizado com base nos dados reais
            'dureza': {'min': 1, 'max': 10},
            'tamanho': {'min': 3, 'max': 45}
        }
        
        # Legenda das funções (código -> descrição)
        self.legenda_funcoes = {
            1: "Impacto - Martelar pregos e objetos",
            2: "Fixação - Aparafusar e fixar componentes",
            3: "Corte - Cortar madeira e materiais", 
            4: "Perfuração - Perfurar buracos em materiais",
            5: "Manipulação - Manipular e segurar objetos",
            6: "Movimento de Solo - Cavar e mover terra",
            7: "Escrita e Leitura - Escrever e marcar",
            8: "Medição e Fixação - Medir e alinhar objetos",
            9: "Outros - Outros usos diversos"
        }
    
    def _funcao_ativacao(self, x: float) -> int:
        """Função de ativação degrau."""
        return 1 if x >= 0 else 0
    
    def _produto_escalar(self, lista1: List[float], lista2: List[float]) -> float:
        """Calcula o produto escalar entre duas listas."""
        return sum(a * b for a, b in zip(lista1, lista2))
    
    def normalizar_valor(self, valor: float, tipo_caracteristica: str) -> float:
        """
        Normaliza um valor numérico entre 0 e 1.
        
        Args:
            valor (float): Valor a ser normalizado
            tipo_caracteristica (str): Tipo da característica
            
        Returns:
            float: Valor normalizado entre 0 e 1
        """
        params = self.normalizacao_params[tipo_caracteristica]
        valor_norm = (valor - params['min']) / (params['max'] - params['min'])
        return max(0.0, min(1.0, valor_norm))
    
    def codificar_funcao_one_hot(self, codigo_funcao: int) -> List[int]:
        """
        Converte o código de função para representação one-hot.
        
        Args:
            codigo_funcao (int): Código da função (1-9)
            
        Returns:
            List[int]: Vetor one-hot de 9 dimensões
        """
        one_hot = [0] * 9
        if 1 <= codigo_funcao <= 9:
            one_hot[codigo_funcao - 1] = 1
        return one_hot
    
    def preparar_features(self, linha_dados: List) -> List[float]:
        """
        Prepara as features de uma linha de dados.
        
        Args:
            linha_dados (List): [nome, peso, dureza, tamanho, cabo, metal, preco, cod_funcao, ...]
            
        Returns:
            List[float]: Vetor de features preparado
        """
        # Características físicas normalizadas
        peso_norm = self.normalizar_valor(float(linha_dados[1]), 'peso')
        dureza_norm = self.normalizar_valor(float(linha_dados[2]), 'dureza')
        tamanho_norm = self.normalizar_valor(float(linha_dados[3]), 'tamanho')
        tem_cabo = float(linha_dados[4])
        material_metalico = float(linha_dados[5])
        
        # Características da função (one-hot encoding)
        codigo_funcao = int(linha_dados[7])
        funcao_one_hot = self.codificar_funcao_one_hot(codigo_funcao)
        
        # Combina todas as features
        features = [peso_norm, dureza_norm, tamanho_norm, tem_cabo, material_metalico]
        features.extend(funcao_one_hot)
        
        return features
    
    def preparar_dados_treinamento(self, dados_brutos: List[List]) -> Tuple[List[List[float]], List[int]]:
        """
        Prepara os dados brutos para treinamento.
        
        Args:
            dados_brutos (List[List]): Dados brutos do dataset
            
        Returns:
            Tuple[List[List[float]], List[int]]: Features processadas e rótulos
        """
        X = []
        y = []
        
        for linha in dados_brutos:
            features = self.preparar_features(linha)
            X.append(features)
            y.append(int(linha[-1]))  # eh_ferramenta
        
        return X, y
    
    def treinar(self, dados_brutos: List[List]) -> None:
        """
        Treina o perceptron com os dados fornecidos.
        
        Args:
            dados_brutos (List[List]): Dados brutos do dataset de treinamento
        """
        print("Iniciando treinamento do Perceptron ...")
        
        # Prepara os dados
        X, y = self.preparar_dados_treinamento(dados_brutos)
        
        n_amostras = len(X)
        n_caracteristicas = len(X[0])
        
        print(f"Dados de treinamento: {n_amostras} amostras, {n_caracteristicas} características")
        print(f"- Características físicas: 5")
        print(f"- Características funcionais (one-hot): 9")
        
        # Inicializa pesos e bias aleatoriamente
        self.pesos = [random.uniform(-0.1, 0.1) for _ in range(n_caracteristicas)]
        self.bias = random.uniform(-0.1, 0.1)
        
        # Treinamento
        for iteracao in range(self.max_iteracoes):
            erros = 0
            
            for i in range(n_amostras):
                # Predição
                saida_linear = self._produto_escalar(X[i], self.pesos) + self.bias
                predicao = self._funcao_ativacao(saida_linear)
                erro = y[i] - predicao
                
                # Atualiza pesos se há erro
                if erro != 0:
                    erros += 1
                    # Regra de aprendizado do perceptron
                    for j in range(n_caracteristicas):
                        self.pesos[j] += self.taxa_aprendizado * erro * X[i][j]
                    self.bias += self.taxa_aprendizado * erro
            
            # Registra histórico
            acuracia_iter = ((n_amostras - erros) / n_amostras) * 100
            self.historico_treinamento.append({
                'iteracao': iteracao + 1,
                'erros': erros,
                'acuracia': acuracia_iter
            })
            
            # Convergência alcançada
            if erros == 0:
                print(f"Convergência alcançada na iteração {iteracao + 1}")
                break
        
        else:
            print(f"Treinamento completo após {self.max_iteracoes} iterações")
        
        # Estatísticas finais
        final_accuracy = self.historico_treinamento[-1]['acuracia']
        print(f"Acurácia final no treinamento: {final_accuracy:.1f}%")
    
    def prever_item(self, item_data: List) -> int:
        """
        Faz predição para um único item.
        
        Args:
            item_data (List): Dados do item
            
        Returns:
            int: Predição (1=ferramenta, 0=não-ferramenta)
        """
        if self.pesos is None:
            raise ValueError("Modelo não foi treinado ainda!")
        
        # Prepara features do item
        features = self.preparar_features(item_data)
        
        # Predição
        saida_linear = self._produto_escalar(features, self.pesos) + self.bias
        return self._funcao_ativacao(saida_linear)
    
    def avaliar_dataset(self, dados_teste: List[List]) -> float:
        """
        Avalia o modelo em um dataset de teste.
        
        Args:
            dados_teste (List[List]): Dados de teste
            
        Returns:
            float: Acurácia em percentual
        """
        if self.pesos is None:
            raise ValueError("Modelo não foi treinado ainda!")
        
        corretas = 0
        total = len(dados_teste)
        detalhes = []
        
        for linha in dados_teste:
            predicao = self.prever_item(linha)
            real = int(linha[-1])
            correto = predicao == real
            
            if correto:
                corretas += 1
            
            detalhes.append({
                'item': linha[0],
                'predicao': predicao,
                'real': real,
                'correto': correto,
                'funcao': self.legenda_funcoes.get(int(linha[7]), "Desconhecida")
            })
        
        # Mostra alguns detalhes da avaliação
        print(f"\nDetalhes da avaliação (primeiros 5 itens):")
        for i, det in enumerate(detalhes[:5]):
            status = ""if det['correto'] else "Errado"
            pred_text = "FERRAMENTA"if det['predicao'] == 1 else "NÃO-FERRAMENTA"
            real_text = "FERRAMENTA"if det['real'] == 1 else "NÃO-FERRAMENTA"
            print(f"{status} {det['item']}: Pred={pred_text}, Real={real_text}")
        
        return (corretas / total) * 100
    
    def mostrar_informacoes_modelo(self) -> None:
        """Exibe informações detalhadas sobre o modelo treinado."""
        if self.pesos is None:
            print("Modelo ainda não foi treinado!")
            return
        
        print("\n"+ "="*60)
        print("INFORMAÇÕES DO MODELO PERCEPTRON ")
        print("="*60)
        
        print(f"Taxa de aprendizado: {self.taxa_aprendizado}")
        print(f"Iterações máximas: {self.max_iteracoes}")
        print(f"Iterações realizadas: {len(self.historico_treinamento)}")
        
        if self.historico_treinamento:
            print(f"Acurácia final: {self.historico_treinamento[-1]['acuracia']:.1f}%")

        print(f"Bias do modelo: {self.bias:.4f}")
        print(f"Total de características: {len(self.pesos)}")
        
        # Análise dos pesos
        print("\nANÁLISE DOS PESOS DAS CARACTERÍSTICAS:")
        nomes_features = [
            "Peso", "Dureza", "Tamanho", "Tem_cabo", "Metal",
            "Func_Impacto", "Func_Fixação", "Func_Corte", "Func_Perfuração",
            "Func_Manipulação", "Func_MovSolo", "Func_Escrita", "Func_Medição", "Func_Outros"
        ]
        
        # Características físicas
        print("\nCaracterísticas Físicas:")
        for i in range(5):
            sinal = "+"if self.pesos[i] >= 0 else ""
            print(f"{nomes_features[i]}: {sinal}{self.pesos[i]:.4f}")
        
        # Características funcionais
        print("\n Características Funcionais:")
        for i in range(5, len(self.pesos)):
            if i < len(nomes_features):
                sinal = "+"if self.pesos[i] >= 0 else ""
                print(f"{nomes_features[i]}: {sinal}{self.pesos[i]:.4f}")
        
        # Legenda das funções
        print("\n LEGENDA DAS FUNÇÕES:")
        for codigo, descricao in self.legenda_funcoes.items():
            print(f"{codigo}: {descricao}")


def carregar_dataset_csv(caminho_arquivo: str) -> Optional[List[List]]:
    """
    Carrega um dataset do arquivo CSV.
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV
        
    Returns:
        Optional[List[List]]: Dados do dataset ou None se houver erro
    """
    try:
        dados = []
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            cabecalho = next(leitor)  # Pula o cabeçalho
            
            for linha in leitor:
                if linha:  # Ignora linhas vazias
                    dados.append(linha)
        
        print(f"Dataset carregado: {caminho_arquivo} ({len(dados)} registros)")
        return dados
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar dataset: {e}")
        return None


def interface_classificacao_manual(modelo: PerceptronFerramentas) -> None:
    """
    Interface para classificação manual de novos itens.
    
    Args:
        modelo (PerceptronFerramentas): Modelo treinado
    """
    print("\n"+ "="*60)
    print("INTERFACE DE CLASSIFICAÇÃO MANUAL DE FERRAMENTAS")
    print("="*60)
    print("Digite as informações do item para classificá-lo.")
    print("Digite 'sair' em qualquer campo para encerrar.")
    
    # Mostra as opções de função
    print(f"\n CÓDIGOS DE FUNÇÃO DISPONÍVEIS:")
    for codigo, descricao in modelo.legenda_funcoes.items():
        print(f"{codigo}: {descricao}")
    print()
    
    while True:
        try:
            nome = input("Nome do item: ")
            if nome.lower() == 'sair':
                break
            
            peso = input("Peso (gramas): ")
            if peso.lower() == 'sair':
                break
            peso = float(peso)
            
            dureza = input("Dureza (1-10): ")
            if dureza.lower() == 'sair':
                break
            dureza = float(dureza)
            
            tamanho = input("Tamanho (cm): ")
            if tamanho.lower() == 'sair':
                break
            tamanho = float(tamanho)
            
            tem_cabo = input("Tem cabo? (1=sim, 0=não): ")
            if tem_cabo.lower() == 'sair':
                break
            tem_cabo = int(tem_cabo)
            
            material_metal = input("Material metálico? (1=sim, 0=não): ")
            if material_metal.lower() == 'sair':
                break
            material_metal = int(material_metal)
            
            cod_funcao = input("Código da função (1-9): ")
            if cod_funcao.lower() == 'sair':
                break
            cod_funcao = int(cod_funcao)
            
            # Verifica se o código é válido
            if cod_funcao not in modelo.legenda_funcoes:
                print("Código de função inválido! Use um código entre 1-9.")
                continue
            
            # Cria item para classificação
            item = [nome, peso, dureza, tamanho, tem_cabo, material_metal, 0.0, cod_funcao]
            
            # Classifica
            predicao = modelo.prever_item(item)
            
            print(f"\n{'='*40}")
            print(f"RESULTADO PARA: {nome}")
            print(f"{'='*40}")
            print(f"Função: {modelo.legenda_funcoes[cod_funcao]}")
            
            if predicao == 1:
                print("CLASSIFICAÇÃO: FERRAMENTA")
                print("Este item foi identificado como uma ferramenta.")
            else:
                print("CLASSIFICAÇÃO: NÃO É FERRAMENTA")
                print("Este item foi identificado como não sendo uma ferramenta.")
            
            print(f"{'='*40}\n")
            
            continuar = input("Classificar outro item? (s/n): ")
            if continuar.lower() not in ['s', 'sim', 'y', 'yes']:
                break
        
        except ValueError as e:
            print(f"Erro: Valor inválido inserido. {e}")
        except KeyboardInterrupt:
            print("\n Operação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


def salvar_resultados_json(modelo: PerceptronFerramentas, total_treino: int, 
                          total_teste: int, acuracia_teste: float) -> None:
    """
    Salva os resultados do treinamento e avaliação em arquivo JSON.
    
    Args:
        modelo (PerceptronFerramentas): Modelo treinado
        total_treino (int): Total de registros de treinamento
        total_teste (int): Total de registros de teste
        acuracia_teste (float): Acurácia no dataset de teste
    """
    try:
        # Prepara dados para salvar
        resultados = {
            "timestamp": datetime.datetime.now().isoformat(),
            "modelo": {
                "tipo": "Perceptron ",
                "taxa_aprendizado": modelo.taxa_aprendizado,
                "max_iteracoes": modelo.max_iteracoes,
                "iteracoes_realizadas": len(modelo.historico_treinamento),
                "convergiu": len(modelo.historico_treinamento) < modelo.max_iteracoes
            },
            "dados": {
                "total_treino": total_treino,
                "total_teste": total_teste,
                "caracteristicas_fisicas": 5,
                "caracteristicas_funcionais": 9,
                "total_caracteristicas": 14
            },
            "performance": {
                "acuracia_treino_final": modelo.historico_treinamento[-1]['acuracia'] if modelo.historico_treinamento else 0,
                "acuracia_teste": acuracia_teste,
                "bias": modelo.bias if modelo.bias else 0
            },
            "historico_treinamento": modelo.historico_treinamento,
            "categorias_funcao": modelo.legenda_funcoes,
            "pesos_modelo": {
                "bias": modelo.bias if modelo.bias else 0,
                "pesos_caracteristicas": modelo.pesos if modelo.pesos else []
            }
        }
        
        # Salva no arquivo JSON
        with open('resultados_treinamento.json', 'w', encoding='utf-8') as arquivo:
            json.dump(resultados, arquivo, indent=2, ensure_ascii=False)
        
        print(f"\n💾 RESULTADOS SALVOS EM: resultados_treinamento.json")
        print(f"📊 Timestamp: {resultados['timestamp']}")
        print(f"🎯 Acurácia Treino: {resultados['performance']['acuracia_treino_final']:.1f}%")
        print(f"🧪 Acurácia Teste: {resultados['performance']['acuracia_teste']:.1f}%")
        
    except Exception as e:
        print(f"❌ Erro ao salvar JSON: {e}")


def main():
    """Função principal do sistema de classificação de ferramentas."""
    print("="*70)
    print("SISTEMA DE CLASSIFICAÇÃO DE FERRAMENTAS - ")
    print("Implementação Perceptron com Códigos Numéricos")
    print("="*70)
    
    # Carrega dataset de treinamento
    dados_treino = carregar_dataset_csv('data/dataset_ferramentas.csv')
    if dados_treino is None:
        print("Erro: Não foi possível carregar o dataset de treinamento.")
        return
    
    # Cria e treina o modelo
    print(f"\nInicializando Perceptron ...")
    modelo = PerceptronFerramentas(taxa_aprendizado=0.1, max_iteracoes=1000)
    
    print("Treinando modelo...")
    modelo.treinar(dados_treino)
    
    # Mostra informações do modelo
    modelo.mostrar_informacoes_modelo()
    
    # Avalia no dataset de teste
    dados_teste = carregar_dataset_csv('data/dataset_teste.csv')
    if dados_teste is not None:
        print(f"\nAVALIAÇÃO NO DATASET DE TESTE")
        print("-"* 50)
        acuracia_teste = modelo.avaliar_dataset(dados_teste)
        print(f"\nACURÁCIA NO DATASET DE TESTE: {acuracia_teste:.1f}%")
    
    # Salva resultados em JSON
    salvar_resultados_json(modelo, len(dados_treino), len(dados_teste) if dados_teste else 0, 
                          acuracia_teste if dados_teste else 0)
    
    # Interface de classificação manual
    interface_classificacao_manual(modelo)
    
    print("\n"+ "="*70)
    print("Obrigado por usar o sistema de classificação!")
    print("="*70)


if __name__ == "__main__":
    main()