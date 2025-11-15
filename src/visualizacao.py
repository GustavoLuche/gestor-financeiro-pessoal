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
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    

def grafico_pizza_despesas(gestor: GestorFinanceiro, salvar: bool = True):
    """Cria gráfico de pizza das despesas por categoria"""
    configurar_estilo()
    despesas = gestor.obter_despesas_por_categoria()
    
    if not despesas:
        print("⚠️  Nenhuma despesa registrada.")
        return
    
    plt.figure()
    plt.pie(despesas.values(), labels=despesas.keys(), autopct='%1.1f%%', startangle=90)
    plt.title('💸 Despesas por Categoria')
    plt.axis('equal')
    
    if salvar:
        Path('reports').mkdir(exist_ok=True)
        plt.savefig('reports/despesas_pizza.png', dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()
    

def grafico_pizza_receitas(gestor: GestorFinanceiro, salvar: bool = True):
    """Cria gráfico de pizza das receitas por categoria"""
    configurar_estilo()
    receitas = gestor.obter_receitas_por_categoria()
    
    if not receitas:
        print("⚠️  Nenhuma receita registrada.")
        return
    
    plt.figure()
    plt.pie(receitas.values(), labels=receitas.keys(), autopct='%1.1f%%', startangle=90)
    plt.title('💵 Receitas por Categoria')
    plt.axis('equal')
    
    if salvar:
        Path('reports').mkdir(exist_ok=True)
        plt.savefig('reports/receitas_pizza.png', dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()
    

def grafico_barras_mensal(gestor: GestorFinanceiro, ano: int, salvar: bool = True):
    """Cria gráfico de barras comparando receitas e despesas mensais"""
    configurar_estilo()
    
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    receitas_mensais = []
    despesas_mensais = []
    
    for mes in range(1, 13):
        transacoes_mes = gestor.obter_transacoes_mes(mes, ano)
        receitas = sum(t.valor for t in transacoes_mes if t.tipo == 'receita')
        despesas = sum(t.valor for t in transacoes_mes if t.tipo == 'despesa')
        receitas_mensais.append(receitas)
        despesas_mensais.append(despesas)
    
    x = range(len(meses))
    width = 0.35
    
    fig, ax = plt.subplots()
    ax.bar([i - width/2 for i in x], receitas_mensais, width, label='Receitas', color='green')
    ax.bar([i + width/2 for i in x], despesas_mensais, width, label='Despesas', color='red')
    
    ax.set_xlabel('Mês')
    ax.set_ylabel('Valor (R$)')
    ax.set_title(f'📊 Receitas vs Despesas - {ano}')
    ax.set_xticks(x)
    ax.set_xticklabels(meses)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    if salvar:
        Path('reports').mkdir(exist_ok=True)
        plt.savefig(f'reports/mensal_{ano}.png', dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()
    

def grafico_evolucao_saldo(gestor: GestorFinanceiro, salvar: bool = True):
    """Cria gráfico de linha mostrando evolução do saldo"""
    configurar_estilo()
    
    if not gestor.transacoes:
        print("⚠️  Nenhuma transação registrada.")
        return
    
    # Ordenar transações por data
    transacoes_ordenadas = sorted(gestor.transacoes, key=lambda t: t.data)
    
    datas = []
    saldos = []
    saldo_acumulado = 0
    
    for t in transacoes_ordenadas:
        if t.tipo == 'receita':
            saldo_acumulado += t.valor
        else:
            saldo_acumulado -= t.valor
        datas.append(t.data)
        saldos.append(saldo_acumulado)
    
    plt.figure()
    plt.plot(datas, saldos, marker='o', linestyle='-', linewidth=2, markersize=4)
    plt.xlabel('Data')
    plt.ylabel('Saldo (R$)')
    plt.title('📈 Evolução do Saldo')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if salvar:
        Path('reports').mkdir(exist_ok=True)
        plt.savefig('reports/evolucao_saldo.png', dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()
    

def relatorio_completo(gestor: GestorFinanceiro):
    """Gera todos os gráficos e salva em reports/"""
    print("📊 Gerando relatórios...")
    from datetime import datetime
    ano_atual = datetime.now().year
    
    grafico_pizza_despesas(gestor, salvar=True)
    print("✅ Gráfico de despesas gerado")
    
    grafico_pizza_receitas(gestor, salvar=True)
    print("✅ Gráfico de receitas gerado")
    
    grafico_barras_mensal(gestor, ano_atual, salvar=True)
    print("✅ Gráfico mensal gerado")
    
    grafico_evolucao_saldo(gestor, salvar=True)
    print("✅ Gráfico de evolução gerado")
    
    print("\n✅ Todos os relatórios foram salvos em reports/")
