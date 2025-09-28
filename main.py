#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Classificação de Ferramentas usando Perceptron

Este é o arquivo principal para executar o sistema de classificação
de ferramentas de uma loja de material de construção.

Autor: Sistema Perceptron
Data: 2025
"""

import sys
import os

# Garante que estamos no diretório correto
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# Adiciona o diretório src ao path para importar os módulos
sys.path.append(os.path.join(current_dir, 'src'))

from classificador_ferramentas import main

if __name__ == "__main__":
    print("=" * 60)
    print("    SISTEMA DE CLASSIFICAÇÃO DE FERRAMENTAS")
    print("    Loja de Material de Construção - Perceptron")
    print("=" * 60)
    print()
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro durante a execução: {e}")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("    Obrigado por usar o sistema!")
    print("=" * 60)