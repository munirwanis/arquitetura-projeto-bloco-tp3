#-*- coding:utf-8 -*-

# 15) Escreva um programa em Python que leia repetidamente N números do teclado. Leia N inicialmente. No final, escreva a média aritmética desses números.

numberList = []

count = int(input('Digite N: '))

for i in range(1,count + 1):
    number = int(input(f'Digite o {i}º número: '))
    numberList.append(number)

print(f'Média aritmética é {sum(numberList) / len(numberList)}.')