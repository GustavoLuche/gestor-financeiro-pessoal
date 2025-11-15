"""
Gerenciador de banco de dados (JSON) para transações financeiras
"""

import json
import pandas as pd
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from .models import Transacao, CategoriaReceita, CategoriaDespesa


class GestorFinanceiro:
    """Gerencia todas as transações financeiras"""
    
    def __init__(self, arquivo_dados: str = "data/transacoes.json"):
        """Inicializa o gestor financeiro"""
        self.arquivo_dados = Path(arquivo_dados)
        self.transacoes: List[Transacao] = []
        self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega transações do arquivo JSON"""
        # Copilot: implementar carregamento de JSON e conversão para lista de Transacao
        
    def salvar_dados(self):
        """Salva transações no arquivo JSON"""
        # Copilot: implementar salvamento da lista de transações em JSON
        
    def adicionar_receita(self, valor: float, categoria: CategoriaReceita, 
                         descricao: str, data: Optional[datetime] = None):
        """Adiciona uma nova receita"""
        # Copilot: criar nova Transacao do tipo 'receita' e adicionar à lista
        
    def adicionar_despesa(self, valor: float, categoria: CategoriaDespesa,
                         descricao: str, data: Optional[datetime] = None):
        """Adiciona uma nova despesa"""
        # Copilot: criar nova Transacao do tipo 'despesa' e adicionar à lista
        
    def obter_saldo_total(self) -> float:
        """Calcula o saldo total (receitas - despesas)"""
        # Copilot: calcular soma de receitas menos soma de despesas
        
    def obter_receitas_total(self) -> float:
        """Calcula o total de receitas"""
        # Copilot: somar todas as transações do tipo 'receita'
        
    def obter_despesas_total(self) -> float:
        """Calcula o total de despesas"""
        # Copilot: somar todas as transações do tipo 'despesa'
        
    def obter_transacoes_mes(self, mes: int, ano: int) -> List[Transacao]:
        """Retorna transações de um mês específico"""
        # Copilot: filtrar transações por mês e ano
        
    def obter_despesas_por_categoria(self) -> dict:
        """Retorna despesas agrupadas por categoria"""
        # Copilot: agrupar despesas por categoria e somar valores
        
    def obter_receitas_por_categoria(self) -> dict:
        """Retorna receitas agrupadas por categoria"""
        # Copilot: agrupar receitas por categoria e somar valores
        
    def exportar_para_excel(self, caminho: str = "reports/relatorio.xlsx"):
        """Exporta transações para arquivo Excel"""
        # Copilot: usar pandas para criar DataFrame e exportar para Excel
        
    def remover_transacao(self, transacao_id: str) -> bool:
        """Remove uma transação pelo ID"""
        # Copilot: encontrar e remover transação da lista pelo ID
