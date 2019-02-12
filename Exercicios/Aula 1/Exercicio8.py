usrInput = input("Digite sua data de nascimento (dd/mm/aaaa): ")
date = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

splitInput = usrInput.split("/")
print("Data: " + splitInput[0] + " de " + date[int(splitInput[1]) - 1] + " de " + splitInput[2])