#-*- coding:utf-8 -*-

# 10) Escreva um programa em Python que leia repetidamente 5 números do teclado e escreva a soma deles no final.

numberList = []

for i in range(1,6):
    number = int(input(f'Digite o {i}º número: '))
    numberList.append(number)

print(f'Soma: {sum(numberList)}')