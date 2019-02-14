#Faça um programa que leia um arquivo de texto, e  realize os seguintes pré-processamentos: tokenização
#remoção de stopwords, remoção de números, remoção de palavras muito grandes (acima de 7 caracteres), remoção de pontuação
#após o pré-processamento exiba esse novo texto em forma de string.

import string
import re

class Exercicio1:

    def __init__(self, text):
        self.originalText = text
        self.finalText = None
        stopWordsFile = open("stopwords.txt")
        self.stopWords = stopWordsFile.read().split("\n")
        stopWordsFile.close()

    def getMainText(self):
        return self.originalText

    def removeFromList(self, removeList):
        for word in removeList:
            self.finalText.remove(word)

    #Tokenização
    def genTokens(self):

        newText = []
        tempWord = ""

        for c in self.originalText:
            if c not in string.punctuation and c not in string.whitespace:
                tempWord = tempWord + c
            elif c in string.whitespace:
                newText.append(tempWord.lower())
                tempWord = ""


        self.finalText = newText

    #Stopwords
    def removeStopWords(self):
        wordsToRemove = []

        for word in self.finalText:
            if word in self.stopWords:
                wordsToRemove.append(word)

        self.removeFromList(wordsToRemove)

    #Remove numbers
    def removeNumbers(self):
        wordsToRemove = []

        for word in self.finalText:
            if any(char.isdigit() for char in word):
                wordsToRemove.append(word)

        self.removeFromList(wordsToRemove)

    #Remove big words
    def removeBigWords(self, wordSize):
        global finalText
        wordsToRemove = []

        for word in self.finalText:
            if len(word) > wordSize:
                wordsToRemove.append(word)

        self.removeFromList(wordsToRemove)

    def getFinishedText(self):
        return self.finalText

    def getOriginalText(self):
        return self.originalText

