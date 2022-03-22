import json
from os import path
from googletrans import Translator
import FileServices as FS


class TranslateService:

    def __init__(self, fileName="Dictionary-en-es.json"):
        self.FileName = FS.CreateFilePath(fileName)
        self.Dictionary = self.ReadFile()

    def ReadFile(self):
        json_object = {}

        fileExists = path.exists(self.FileName)
        if fileExists:
            with open(self.FileName, 'r') as inFile:
                json_object = json.load(inFile)

        return json_object

    def GetDictionary(self):
        return self.Dictionary

    def Translate(self, wordList):
        translator = Translator()
        newWordAdded = False
        for word in wordList:
            if not word in self.Dictionary:
                translated = translator.translate(word, dest="es", src="en")
                self.Dictionary[word] = translated.text
                newWordAdded = True

        if newWordAdded:
            self.WriteFile()

        return self.Dictionary

    def WriteFile(self):
        with open(self.FileName, "w", encoding='utf8') as outFile:
            json.dump(self.Dictionary, outFile, ensure_ascii=False)
