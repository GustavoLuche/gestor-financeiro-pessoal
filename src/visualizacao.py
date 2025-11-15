"""
Módulo para visualização de dados financeiros
"""

import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, List
from pathlib import Path
from .database import GestorFinanceiro


def configurar_estilo():
    """Configura o estilo dos gráficos"""
    # Copilot: configurar estilo matplotlib (tamanho de fonte, cores, etc)
    

def grafico_pizza_despesas(gestor: GestorFinanceiro, salvar: bool = True):
    """Cria gráfico de pizza das despesas por categoria"""
    # Copilot: criar gráfico de pizza com despesas por categoria
    # usar gestor.obter_despesas_por_categoria()
    

def grafico_pizza_receitas(gestor: GestorFinanceiro, salvar: bool = True):
    """Cria gráfico de pizza das receitas por categoria"""
    # Copilot: criar gráfico de pizza com receitas por categoria
    

def grafico_barras_mensal(gestor: GestorFinanceiro, ano: int, salvar: bool = True):
    """Cria gráfico de barras comparando receitas e despesas mensais"""
    # Copilot: criar gráfico de barras com receitas vs despesas por mês
    

def grafico_evolucao_saldo(gestor: GestorFinanceiro, salvar: bool = True):
    """Cria gráfico de linha mostrando evolução do saldo"""
    # Copilot: criar gráfico de linha mostrando saldo acumulado ao longo do tempo
    

def relatorio_completo(gestor: GestorFinanceiro):
    """Gera todos os gráficos e salva em reports/"""
    # Copilot: chamar todas as funções de gráfico
    print("📊 Gerando relatórios...")
