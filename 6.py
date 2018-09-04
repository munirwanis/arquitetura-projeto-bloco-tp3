#-*- coding:utf-8 -*-

# 6) Escreva um programa em Python que leia três números e indique qual deles é o menor.

firstNumber = int(input('Digite o primeiro número: '))
secondNumber = int(input('Digite o segundo número: '))
thirdNumber = int(input('Digite o terceiro número: '))

if firstNumber < secondNumber and firstNumber < thirdNumber:
    print(f'Número {firstNumber} é menor.')
elif secondNumber < firstNumber and secondNumber < thirdNumber:
    print(f'Número {secondNumber} é menor.')
elif thirdNumber < firstNumber and thirdNumber < secondNumber:
    print(f'Número {thirdNumber} é menor.')

