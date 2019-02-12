#Faça um programa que leia 4 notas, mostre as notas e a média na tela.

from random import randint

notas = []
total = 0

for i in range(4):
    notas.append(randint(0,11))
    total += notas[i]


total = total / 4
print("Notas: " + str(notas))
print("Media: " + str(total))

