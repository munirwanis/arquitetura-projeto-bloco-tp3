#-*- coding:utf-8 -*-

# 11) Escreva um programa em Python que leia repetidamente 5 números do teclado e indique, para cada, se é positivo.

for i in range(1,6):
    number = int(input(f'Digite o {i}º número: '))
    print(f'Número é {"positivo" if number >= 0 else "negativo"}.')