#Faça um programa que leia um vetor de 10 numeros e mostre-os na ordem inversa.

from random import randint

listainicial = []
listafinal = []

for i in range(10):
    listainicial.append(randint(0, 10))

for i in reversed(listainicial):
    listafinal.append(i)

print("Lista inicial: " + str(listainicial))
print("Lista final: " + str(listafinal))