#-*- coding:utf-8 -*-

# 5) Escreva um programa em Python que leia dois números e indique qual deles é o maior.

firstNumber = int(input('Digite o primeiro número: '))
secondNumber = int(input('Digite o segundo número: '))

if firstNumber > secondNumber:
    print(f'Número {firstNumber} é maior.')
else:
    print(f'Número {secondNumber} é maior.')
