#-*- coding:utf-8 -*-

# 16) Escreva um programa em Python que leia números positivos até que um valor negativo seja lido. No final, apresente o resultado da soma deles (não inclua o número negativo).

number = 0
numberSum = 0

while number >= 0:
    number = int(input('Digite o número: '))
    if number > 0:
        numberSum += number

print(f'Soma é {numberSum}.')