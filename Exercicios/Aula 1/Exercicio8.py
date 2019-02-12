#Data por extenso.
#Faça um programa que solicite a data de nascimento (dd/mm/aa) do usuario e imprima a data com o nome do mes por extenso

usrInput = input("Digite sua data de nascimento (dd/mm/aaaa): ")
date = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

splitInput = usrInput.split("/")
print("Data: " + splitInput[0] + " de " + date[int(splitInput[1]) - 1] + " de " + splitInput[2])