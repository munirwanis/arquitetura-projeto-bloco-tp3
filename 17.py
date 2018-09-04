#-*- coding:utf-8 -*-

# 17) Escreva um programa em Python que:
# a. gera uma lista de nome de cores e depois imprima ela. As cores são: azul, vermelho, verde, amarelo, violeta, marrom, branco e preto.
# b. Em seguida, remova a cor ‘marrom’ desta lista e imprima a lista após esta operação.
# c. Em seguida, adicione a cor ‘cinza’ na lista e imprima a lista a lista após esta operação.
# d. Em seguida, altere a cor ‘violeta’ para ‘rosa’.
# e. Em seguida, leia um nome de cor do teclado e a remova da lista. Não esqueça de checar se ela existe na lista.

number = 0
numberSum = 0
colors = ['azul', 'vermelho', 'verde', 'amarelo', 'violeta', 'marrom', 'branco', 'preto']
print(colors)

colors.remove('marrom')
print(colors)

colors.append('cinza')
print(colors)

colors[:] = ['rosa' if x == 'violeta' else x for x in colors]
print(colors)

colorToRemove = input('Digite a cor para remover: ')
if colorToRemove in colors: colors.remove(colorToRemove)
print(colors)