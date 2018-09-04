#-*- coding:utf-8 -*-

# 19) Escreva um programa em Python que leia nome de pessoas repetidamente e crie uma lista com estes nomes.
# No final, imprima esta lista. A leitura termina quando a palavra ‘sair’ for digitada.

name = ''
names = []
while name.lower() != 'sair':
    name = input('Digite um nome: ')
    if name.lower() != 'sair': names.append(name)

print(names)