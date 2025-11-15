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
    # Copilot: solicitar dados ao usuário e chamar gestor.adicionar_receita()
    # mostrar opções de CategoriaReceita
    

def adicionar_despesa(gestor: GestorFinanceiro):
    """Interface para adicionar despesa"""
    # Copilot: solicitar dados ao usuário e chamar gestor.adicionar_despesa()
    # mostrar opções de CategoriaDespesa
    

def ver_saldo(gestor: GestorFinanceiro):
    """Exibe o saldo atual"""
    # Copilot: mostrar receitas, despesas e saldo total formatados
    

def relatorio_mensal(gestor: GestorFinanceiro):
    """Exibe relatório do mês"""
    # Copilot: pedir mês/ano e mostrar transações do período
    

def listar_transacoes(gestor: GestorFinanceiro):
    """Lista todas as transações"""
    # Copilot: mostrar todas as transações formatadas com índice
    

def remover_transacao(gestor: GestorFinanceiro):
    """Remove uma transação"""
    # Copilot: listar transações, pedir ID e remover
    

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
