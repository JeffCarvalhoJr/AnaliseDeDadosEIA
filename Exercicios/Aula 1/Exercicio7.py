#Nome ao contrario em maiusculas.
#Faça um programa que permita ao usuario digitar o seu nome e em seguida mostre o nome do usuario de trás pra frente
#utilizando somente letras maiusculas

string1 = input("Digite seu nome: ")
stringResult = string1[::-1].upper()
print(stringResult)