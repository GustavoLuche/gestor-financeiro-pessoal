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
        if not self.arquivo_dados.exists():
            self.arquivo_dados.parent.mkdir(parents=True, exist_ok=True)
            self.transacoes = []
            return
        
        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.transacoes = [Transacao.from_dict(t) for t in dados]
        except (json.JSONDecodeError, FileNotFoundError):
            self.transacoes = []
        
    def salvar_dados(self):
        """Salva transações no arquivo JSON"""
        self.arquivo_dados.parent.mkdir(parents=True, exist_ok=True)
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            dados = [t.to_dict() for t in self.transacoes]
            json.dump(dados, f, ensure_ascii=False, indent=2)
        
    def adicionar_receita(self, valor: float, categoria: CategoriaReceita, 
                         descricao: str, data: Optional[datetime] = None):
        """Adiciona uma nova receita"""
        if data is None:
            data = datetime.now()
        
        transacao = Transacao(
            data=data,
            valor=valor,
            categoria=categoria.value,
            descricao=descricao,
            tipo='receita'
        )
        self.transacoes.append(transacao)
        self.salvar_dados()
        
    def adicionar_despesa(self, valor: float, categoria: CategoriaDespesa,
                         descricao: str, data: Optional[datetime] = None):
        """Adiciona uma nova despesa"""
        if data is None:
            data = datetime.now()
        
        transacao = Transacao(
            data=data,
            valor=valor,
            categoria=categoria.value,
            descricao=descricao,
            tipo='despesa'
        )
        self.transacoes.append(transacao)
        self.salvar_dados()
        
    def obter_saldo_total(self) -> float:
        """Calcula o saldo total (receitas - despesas)"""
        return self.obter_receitas_total() - self.obter_despesas_total()
        
    def obter_receitas_total(self) -> float:
        """Calcula o total de receitas"""
        return sum(t.valor for t in self.transacoes if t.tipo == 'receita')
        
    def obter_despesas_total(self) -> float:
        """Calcula o total de despesas"""
        return sum(t.valor for t in self.transacoes if t.tipo == 'despesa')
        
    def obter_transacoes_mes(self, mes: int, ano: int) -> List[Transacao]:
        """Retorna transações de um mês específico"""
        return [t for t in self.transacoes if t.data.month == mes and t.data.year == ano]
        
    def obter_despesas_por_categoria(self) -> dict:
        """Retorna despesas agrupadas por categoria"""
        categorias = {}
        for t in self.transacoes:
            if t.tipo == 'despesa':
                if t.categoria not in categorias:
                    categorias[t.categoria] = 0
                categorias[t.categoria] += t.valor
        return categorias
        
    def obter_receitas_por_categoria(self) -> dict:
        """Retorna receitas agrupadas por categoria"""
        categorias = {}
        for t in self.transacoes:
            if t.tipo == 'receita':
                if t.categoria not in categorias:
                    categorias[t.categoria] = 0
                categorias[t.categoria] += t.valor
        return categorias
        
    def exportar_para_excel(self, caminho: str = "reports/relatorio.xlsx"):
        """Exporta transações para arquivo Excel"""
        if not self.transacoes:
            print("Nenhuma transação para exportar.")
            return
        
        Path(caminho).parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame([t.to_dict() for t in self.transacoes])
        df['data'] = pd.to_datetime(df['data'])
        df = df.sort_values('data', ascending=False)
        df.to_excel(caminho, index=False)
        
    def remover_transacao(self, transacao_id: str) -> bool:
        """Remove uma transação pelo ID"""
        for i, t in enumerate(self.transacoes):
            if t.id == transacao_id:
                self.transacoes.pop(i)
                self.salvar_dados()
                return True
        return False
