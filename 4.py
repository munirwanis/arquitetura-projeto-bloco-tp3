#-*- coding:utf-8 -*-

# 4) Escreva um programa em Python que leia um número (inteiro) e verifique se ele é positivo ou negativo. Se for positivo, indique se ele é par ou ímpar.

number = int(input('Digite um número: '))

if number > 0:
    if number % 2 == 0:
        print('Número é par.')
    else:
        print('Número é ímpar.')
