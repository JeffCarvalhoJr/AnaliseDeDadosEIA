usrInput = input()
usrInput = usrInput.replace(" ", "").lower()
palindromo = usrInput[::-1]

if(usrInput == palindromo):
    print("É um palindromo")
else:
    print("Não é um palindromo")