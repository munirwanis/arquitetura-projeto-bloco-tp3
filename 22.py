#-*- coding:utf-8 -*-

# 22) Escreva um programa em Python que pergunte repetidamente se o usuário quer
# adicionar (a), remover (r), modificar (m) ou imprimir (i) elementos de uma lista.
# Adicione também a opção de sair(s), para sair do programa.
# Dependendo da resposta, o seu programa deve realizar a operação desejada.
# A lista inicialmente encontra-se vazia.

notes = []
menu = """
(a) - Adicionar
(r) - Remover
(m) - Modificar
(i) - Imprimir
(s) - Sair
"""

option = ''
collection = []

while option != 's':
    option = input(menu).lower()
    if option == 'a':
        collection.append(input('Inserir dado: '))
    elif option == 'r':
        to_remove = input('Remover dado: ')
        if to_remove in collection: collection.remove(to_remove)
    elif option == 'm':
        to_search = input('Qual dado? ')
        to_modify = input('Modificar por: ')
        collection[:] = [to_modify if x == to_search else x for x in collection]
    elif option == 'i':
        print(collection)