#-*- coding:utf-8 -*-

# 12) Escreva um programa em Python que leia repetidamente 5 números (inteiros) do teclado e indique, para cada, se é par ou ímpar.

for i in range(1,6):
    number = int(input(f'Digite o {i}º número: '))
    print(f'Número é {"par" if number % 2 == 0 else "ímpar"}.')