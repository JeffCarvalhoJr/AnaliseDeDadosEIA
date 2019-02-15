#Faça o mesmo que na questao anterior utilizando o Spacy, adicionalmente faça a lematização. (Checklist: Tokenização, Remoção de Stopwords, Remoção de numeros, Remoção de palavras grandes

import spacy

class Exercicio2:

    def __init__(self, text):

        self.nlp = spacy.load('en')
        self.originalText = self.nlp(text)
        self.finalText = None

    def removeFromList(self, removeList):
        for word in removeList:
            self.finalText.remove(word)


    #generates tokens and stopwords
    def genToken(self):
        self.finalText = [token.text.lower() for token in self.originalText if not(token.is_stop or token.is_punct)]

    def getLemmatization(self):
        lemmas = [token.lemma_.lower() for token in self.nlp(" ".join(self.finalText))]
        return lemmas

    # Remove numbers
    def removeNumbers(self):

        wordsToRemove = []
        for word in self.finalText:
            if any(char.isdigit() for char in word):
                wordsToRemove.append(word)

        self.removeFromList(wordsToRemove)

    # Remove big words
    def removeBigWords(self, wordSize):
        global finalText
        wordsToRemove = []

        for word in self.finalText:
            if len(word) > wordSize:
                wordsToRemove.append(word)

        self.removeFromList(wordsToRemove)

    def getFinalText(self):
        return self.finalText