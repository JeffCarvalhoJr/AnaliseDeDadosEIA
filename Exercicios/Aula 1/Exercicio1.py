#Faça um programa que baseado no exemplo anterior ( [i for i in range(10) if i%2==0]
#exiba uma lista de numeros impares.

from random import randint

for i in range(10):
    listainicial = randint(0, 10)

impares = [i for i in range(10) if i%2 == 1]
print(impares)