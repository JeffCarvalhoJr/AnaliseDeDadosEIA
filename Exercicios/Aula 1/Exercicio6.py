from collections import Counter

string1 = input()
string2 = input()

print("String 1: " + string1 + " Tem tamanho: " + str(len(string1)))
print("String 2: " + string2 + " Tem tamanho: " + str(len(string2)))

if Counter(string1) == Counter(string2):
    print("As strings tem o mesmo conteudo")
else:
    print("As strings não tem o mesmo conteudo")