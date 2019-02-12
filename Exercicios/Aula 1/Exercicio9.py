#Palindromo.
#Um palíndromo é uma seqüência de caracteres cuja leitura é
#idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e
#OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
#ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma
#onde os espaços foram ignorados. Faça um programa que leia uma sequencia de caracteres e diga se é um palindromo ou nao

usrInput = input()
usrInput = usrInput.replace(" ", "").lower()
palindromo = usrInput[::-1]

if(usrInput == palindromo):
    print("É um palindromo")
else:
    print("Não é um palindromo")