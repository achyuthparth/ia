#import json
#from googletrans import Translator

#translator = Translator()

#testWord = ["apples are yummy", "i like eating them"]

#translated = ""

#translated = translator.translate(testWord, dest = 'es', src = 'en')


#translator = Translator(service_urls=['translate.googleapis.com'])
#translated = translator.translate("perro", dest='en')

#print(translated.text)
#print(translated.pronunciation)


#def readFile(self, wordList):


#def VocabTrans(srcLang, destLang, wordList):
#    for each in wordList:
import json
from os import path
from googletrans import Translator

translator = Translator()

class TranslateFile:

    def __init__(self, fileName="D:\\Users\\achyu\\Source\\repos\\ia\\src\\Dictionary-es-en.json"):
        self.FileName = fileName
        self.Dictionary = ReadFile()

    def ReadFile(self):
        # TODO: check if file exists

        with open(self.FileName, 'r') as inFile:
            json_object = json.load(inFile)
            return json_object

    def GetDictionary(self):
        return self.Dictionary

    def Translate(self, wordList):
        newWordAdded = False
        for word in wordList:
            if not word in self.Dictionary:
                translated = translator.translate("es", "en", word)
                self.Dictionary[word] = translated.text
                newWordAdded = True

        if newWordAdded:
            self.WriteFile()

        return self.Dictionary

    def WriteFile(self):
        with open(self.FileName, 'w') as outfile:
            json.dump(dictionary, outfile)

