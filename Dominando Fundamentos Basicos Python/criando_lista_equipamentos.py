''' Autor: André Holanda
    Projeto: Criando uma Lista de Equipamentos
    Data: 17/06/2025

    Desafio: Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

    Requisitos:
        Entrada:
            O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

        Saída:
            Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.
'''
# Lista para salvar os itens
itens = []

print("Informe os 3 itens que serão adicionados a lista")
# Loop que solicita os itens ao usuário
for i in range(1,4):
    item = input(f"Item {i}º: ")
    itens.append(item)
# Exibe a lista de itens
print("\nLista de Equipamentos:")  
for item in itens:
    print(f"- {item}")