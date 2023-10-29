class Text:
    text = None

    def __init__(self, text):
        self.text = text

    def getLen(self):
        return len(self.text)
    
    def getLenNonSpace(self):
        return len((self.text).replace(' ', ''))
    
    def getSpaces(self):
        count = 0
        for i in self.text:
            if i == ' ':
                count += 1

        return count
    
    def getRightLenSymbols(self):
        return self.getLen() - self.getSpaces()
    
    def getWords(self):
        return (self.text).split()
    
    def getSentence(self):
        return (self.text).split('.')
    
text = Text("Здарова, корова. Меня зовут ЧОРТ")

print(text.getLen())
print(text.getLenNonSpace())
print(text.getSpaces())
print(text.getRightLenSymbols())
print(text.getWords())
print(text.getSentence())