#-*- coding:utf-8 -*-

# 3) Escreva um programa em Python que leia um número (inteiro) e indique se ele é par ou ímpar.

number = int(input('Digite um número: '))

if number % 2 == 0:
    print('Número é par.')
else:
    print('Número é ímpar.')
