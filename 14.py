#-*- coding:utf-8 -*-

# 14) Escreva um programa em Python que leia repetidamente N números do teclado e escreva o valor do dobro destes números. Leia N inicialmente.

numberList = []

count = int(input('Digite N: '))

for i in range(1,count + 1):
    number = int(input(f'Digite o {i}º número: '))
    print(f'Valor dobrado é {number * 2}.')