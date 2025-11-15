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
            import hashlib
            import time
            timestamp = str(time.time()).encode()
            self.id = hashlib.md5(timestamp).hexdigest()[:12]
            
    def to_dict(self) -> dict:
        """Converte a transação para dicionário"""
        return {
            'id': self.id,
            'data': self.data.isoformat(),
            'valor': self.valor,
            'categoria': self.categoria,
            'descricao': self.descricao,
            'tipo': self.tipo
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        """Cria transação a partir de dicionário"""
        data_copy = data.copy()
        data_copy['data'] = datetime.fromisoformat(data_copy['data'])
        return cls(**data_copy)
        
    def __str__(self) -> str:
        """Representação em string da transação"""
        simbolo = "💵" if self.tipo == "receita" else "💸"
        data_fmt = self.data.strftime("%d/%m/%Y")
        return f"{simbolo} {data_fmt} | R$ {self.valor:.2f} | {self.categoria} | {self.descricao}"
