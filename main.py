"""
Sistema de Gestão Financeira Pessoal
Arquivo principal com interface de linha de comando
"""

import os
from datetime import datetime
from src.database import GestorFinanceiro
from src.models import CategoriaReceita, CategoriaDespesa
from src.visualizacao import relatorio_completo


def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("💰 GESTOR FINANCEIRO PESSOAL")
    print("="*50)
    print("\n1. 💵 Adicionar Receita")
    print("2. 💸 Adicionar Despesa")
    print("3. 💰 Ver Saldo Atual")
    print("4. 📊 Relatório Mensal")
    print("5. 📈 Gerar Gráficos")
    print("6. 📋 Listar Todas as Transações")
    print("7. 📥 Exportar para Excel")
    print("8. 🗑️  Remover Transação")
    print("0. ❌ Sair")
    print("="*50)


def adicionar_receita(gestor: GestorFinanceiro):
    """Interface para adicionar receita"""
    print("\n💵 ADICIONAR RECEITA")
    print("="*50)
    
    # Mostrar categorias
    print("\nCategorias disponíveis:")
    categorias = list(CategoriaReceita)
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat.value}")
    
    try:
        # Solicitar dados
        cat_idx = int(input("\nEscolha a categoria (número): ")) - 1
        categoria = categorias[cat_idx]
        
        valor = float(input("Valor (R$): "))
        descricao = input("Descrição: ")
        
        gestor.adicionar_receita(valor, categoria, descricao)
        print("\n✅ Receita adicionada com sucesso!")
    except (ValueError, IndexError):
        print("\n❌ Erro: Entrada inválida!")
    

def adicionar_despesa(gestor: GestorFinanceiro):
    """Interface para adicionar despesa"""
    print("\n💸 ADICIONAR DESPESA")
    print("="*50)
    
    # Mostrar categorias
    print("\nCategorias disponíveis:")
    categorias = list(CategoriaDespesa)
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat.value}")
    
    try:
        # Solicitar dados
        cat_idx = int(input("\nEscolha a categoria (número): ")) - 1
        categoria = categorias[cat_idx]
        
        valor = float(input("Valor (R$): "))
        descricao = input("Descrição: ")
        
        gestor.adicionar_despesa(valor, categoria, descricao)
        print("\n✅ Despesa adicionada com sucesso!")
    except (ValueError, IndexError):
        print("\n❌ Erro: Entrada inválida!")
    

def ver_saldo(gestor: GestorFinanceiro):
    """Exibe o saldo atual"""
    print("\n💰 SALDO ATUAL")
    print("="*50)
    
    receitas = gestor.obter_receitas_total()
    despesas = gestor.obter_despesas_total()
    saldo = gestor.obter_saldo_total()
    
    print(f"\n💵 Total de Receitas:  R$ {receitas:,.2f}")
    print(f"💸 Total de Despesas:  R$ {despesas:,.2f}")
    print(f"{'='*50}")
    
    if saldo >= 0:
        print(f"💰 Saldo Atual:        R$ {saldo:,.2f} ✅")
    else:
        print(f"⚠️  Saldo Atual:        R$ {saldo:,.2f} ❌")
    

def relatorio_mensal(gestor: GestorFinanceiro):
    """Exibe relatório do mês"""
    print("\n📊 RELATÓRIO MENSAL")
    print("="*50)
    
    try:
        mes = int(input("\nMês (1-12): "))
        ano = int(input("Ano: "))
        
        transacoes = gestor.obter_transacoes_mes(mes, ano)
        
        if not transacoes:
            print(f"\n⚠️  Nenhuma transação encontrada para {mes:02d}/{ano}")
            return
        
        receitas = sum(t.valor for t in transacoes if t.tipo == 'receita')
        despesas = sum(t.valor for t in transacoes if t.tipo == 'despesa')
        
        print(f"\n📅 Período: {mes:02d}/{ano}")
        print(f"\n💵 Receitas: R$ {receitas:,.2f}")
        print(f"💸 Despesas: R$ {despesas:,.2f}")
        print(f"💰 Saldo: R$ {receitas - despesas:,.2f}")
        
        print(f"\n📋 Transações ({len(transacoes)}):")
        print("="*50)
        for t in sorted(transacoes, key=lambda x: x.data):
            print(t)
            
    except ValueError:
        print("\n❌ Erro: Entrada inválida!")
    

def listar_transacoes(gestor: GestorFinanceiro):
    """Lista todas as transações"""
    print("\n📋 TODAS AS TRANSAÇÕES")
    print("="*50)
    
    if not gestor.transacoes:
        print("\n⚠️  Nenhuma transação registrada.")
        return
    
    transacoes_ordenadas = sorted(gestor.transacoes, key=lambda t: t.data, reverse=True)
    
    print(f"\nTotal: {len(transacoes_ordenadas)} transações\n")
    
    for i, t in enumerate(transacoes_ordenadas, 1):
        print(f"{i}. {t} [ID: {t.id}]")
    

def remover_transacao(gestor: GestorFinanceiro):
    """Remove uma transação"""
    print("\n🗑️  REMOVER TRANSAÇÃO")
    print("="*50)
    
    if not gestor.transacoes:
        print("\n⚠️  Nenhuma transação registrada.")
        return
    
    # Listar transações
    transacoes_ordenadas = sorted(gestor.transacoes, key=lambda t: t.data, reverse=True)
    print("\nTransações disponíveis:\n")
    
    for i, t in enumerate(transacoes_ordenadas, 1):
        print(f"{i}. {t}")
    
    try:
        idx = int(input("\nNúmero da transação para remover (0 para cancelar): "))
        
        if idx == 0:
            print("\n❌ Operação cancelada.")
            return
        
        if 1 <= idx <= len(transacoes_ordenadas):
            transacao = transacoes_ordenadas[idx - 1]
            if gestor.remover_transacao(transacao.id):
                print("\n✅ Transação removida com sucesso!")
            else:
                print("\n❌ Erro ao remover transação.")
        else:
            print("\n❌ Número inválido!")
    except ValueError:
        print("\n❌ Erro: Entrada inválida!")
    

def main():
    """Função principal do programa"""
    gestor = GestorFinanceiro()
    
    while True:
        limpar_tela()
        exibir_menu()
        
        escolha = input("\n👉 Escolha uma opção: ").strip()
        
        if escolha == "1":
            adicionar_receita(gestor)
        elif escolha == "2":
            adicionar_despesa(gestor)
        elif escolha == "3":
            ver_saldo(gestor)
        elif escolha == "4":
            relatorio_mensal(gestor)
        elif escolha == "5":
            print("\n📊 Gerando gráficos...")
            relatorio_completo(gestor)
            print("✅ Gráficos salvos em reports/")
        elif escolha == "6":
            listar_transacoes(gestor)
        elif escolha == "7":
            gestor.exportar_para_excel()
            print("\n✅ Dados exportados para reports/relatorio.xlsx")
        elif escolha == "8":
            remover_transacao(gestor)
        elif escolha == "0":
            print("\n👋 Até logo!")
            break
        else:
            print("\n❌ Opção inválida!")
        
        input("\n⏎ Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
