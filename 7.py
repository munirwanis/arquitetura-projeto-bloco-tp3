#-*- coding:utf-8 -*-

# 7) Escreva um programa em Python que leia 5 números e escreva a média aritmética entre eles.

numberList = []

for i in range(1,6):
    numberList.append(i)

print(f'Lista: {numberList}')
print(f'Média aritmética: {sum(numberList) / len(numberList)}')