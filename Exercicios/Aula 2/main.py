from Exercicio1 import Exercicio1
from Exercicio2 import Exercicio2

#
mainFile = open("imdb/neg/9_4.txt", "r")
mainText = mainFile.read()
mainFile.close()

###Exercicio 1 ###
#exercicio1 = Exercicio1(mainText)
#exercicio1.genTokens()
#exercicio1.removeStopWords()
#exercicio1.removeNumbers()
#exercicio1.removeBigWords(7)

#print("Texto original: \n\n" + str(exercicio1.getOriginalText()))
#print(exercicio1.getFinishedText())

###Exercicio 2 ####
exercicio2 = Exercicio2(mainText)
exercicio2.genToken()
exercicio2.removeNumbers()
exercicio2.removeBigWords(7)



print(exercicio2.getFinalText())
print("\n\n\nLemmas: ")
print(exercicio2.getLemmatization())