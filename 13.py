#-*- coding:utf-8 -*-

# 13) Escreva um programa em Python que leia repetidamente 5 números do teclado e indique, no final, se a média aritmética desses números é igual, maior ou menor que 6.

numberList = []

for i in range(1,6):
    number = int(input(f'Digite o {i}º número: '))
    numberList.append(number)

result = sum(numberList) / len(numberList)

if result > 6:
    print('Média é maior do que 6.')
elif result < 6:
    print('Média é menor do que 6.')
else:
    print('Média é igual a 6.')