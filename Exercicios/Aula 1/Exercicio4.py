from random import randint

numeroDeAlunos = int(input())
listaAlunos = []
listaMedias = []
count = 0

for i in range(numeroDeAlunos):
    listaAlunos.append([])
    listaMedias.append(0)
    for j in range(4):
        listaAlunos[i].append(randint(0, 10))
        listaMedias[i] += listaAlunos[i][j]

for i in range(numeroDeAlunos):
    print("Notas aluno " + str(i) + ": " + str(listaAlunos[i]))
    print("Media aluno " + str(i) + ": " + str(listaMedias[i] / 4))

    if((listaMedias[i] / 4) > 7):
        count += 1

print("Numero de alunos com media maior que 7: " + str(count))