#Tamanho de strings.
#Faça um programa que leia 2 strings e informe o conteudo delas seguido do seu comprimento.
#Informe tambem se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteudo.

from collections import Counter

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print("String 1: " + string1 + " Tem tamanho: " + str(len(string1)))
print("String 2: " + string2 + " Tem tamanho: " + str(len(string2)))

if Counter(string1) == Counter(string2):
    print("As strings tem o mesmo conteudo")
else:
    print("As strings não tem o mesmo conteudo")