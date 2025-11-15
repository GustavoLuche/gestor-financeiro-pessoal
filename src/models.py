"""
Modelos de dados para o sistema de finanças pessoais
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Optional


class CategoriaReceita(Enum):
    """Categorias de receitas disponíveis"""
    SALARIO = "Salário"
    FREELANCE = "Freelance"
    INVESTIMENTOS = "Investimentos"
    VENDAS = "Vendas"
    BONUS = "Bônus"
    OUTROS = "Outros"


class CategoriaDespesa(Enum):
    """Categorias de despesas disponíveis"""
    MORADIA = "Moradia"
    ALIMENTACAO = "Alimentação"
    TRANSPORTE = "Transporte"
    SAUDE = "Saúde"
    EDUCACAO = "Educação"
    LAZER = "Lazer"
    VESTUARIO = "Vestuário"
    CONTAS = "Contas e Serviços"
    INVESTIMENTOS = "Investimentos"
    OUTROS = "Outros"


@dataclass
class Transacao:
    """Representa uma transação financeira (receita ou despesa)"""
    data: datetime
    valor: float
    categoria: str
    descricao: str
    tipo: str  # 'receita' ou 'despesa'
    id: Optional[str] = None
    
    def __post_init__(self):
        """Gera ID único se não fornecido"""
        if self.id is None:
            # Copilot: gerar ID único baseado em timestamp e hash
            import hashlib
            import time
            
    def to_dict(self) -> dict:
        """Converte a transação para dicionário"""
        # Copilot: converter para dict com data em string ISO format
        
    @classmethod
    def from_dict(cls, data: dict):
        """Cria transação a partir de dicionário"""
        # Copilot: criar instância a partir de dict, convertendo string de data para datetime
        
    def __str__(self) -> str:
        """Representação em string da transação"""
        # Copilot: criar string formatada com todos os dados da transação
