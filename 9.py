#-*- coding:utf-8 -*-

# 9) Escreva um programa em Python que escreva na tela os números de 1 a 10. Use a estrutura de repetição while.

numberList = []
number = 1

while number < 11:
    numberList.append(number)
    number += 1

print(f'Lista: {numberList}')