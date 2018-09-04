#-*- coding:utf-8 -*-

# 20) Escreva um programa em Python que leia uma sequência de números do teclado e os armazene em uma lista.
# Em seguida, indique qual o maior valor dela.

numbersString = input('Digite números separado por `,`: ').split(',')
numbers = list(map(int, numbersString))

print(f'O maior valor da lista é {max(numbers)}')