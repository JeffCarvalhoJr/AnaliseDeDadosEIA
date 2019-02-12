from random import randint

listainicial = []
listafinal = []

for i in range(10):
    listainicial.append(randint(0, 10))

def middle(lista):
    return lista[1:-1]

listafinal = middle(listainicial)

print("Lista inicial: " + str(listainicial))
print("Lista final: " + str(klistafinal))