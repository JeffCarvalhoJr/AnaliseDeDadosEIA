from Exercicio1 import Exercicio1

#
mainFile = open("imdb/neg/9_4.txt", "r")
mainText = mainFile.read()
mainFile.close()

###Exercicio 1 ###
exercicio1 = Exercicio1(mainText)
exercicio1.genTokens()
exercicio1.removeStopWords()
exercicio1.removeNumbers()
exercicio1.removeBigWords(7)

print("Texto original: \n\n" + str(exercicio1.getOriginalText()))
print(exercicio1.getFinishedText())

###