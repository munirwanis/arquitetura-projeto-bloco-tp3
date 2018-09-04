#-*- coding:utf-8 -*-

# 21) Escreva um programa em Python que leia as notas de uma turma de 10 estudantes
# e depois imprima as notas que são maiores do que a média da turma.

notes = []

for i in range(1, 11):
    note = float(input(f'Digite a nota do {i}º aluno: '))
    notes.append(note)

classNote = sum(notes) / len(notes)
greaterNotes = [i for i in notes if i >= classNote]
print(f'As maiores notas são: {greaterNotes}')