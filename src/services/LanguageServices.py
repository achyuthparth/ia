
"""LanguageServices.py: This file has classes and methods for Vocabulary management."""

__author__      = "Achyuthaa Parthasarathy"

import json
from os import path

class VocabAlreadyExists(Exception): pass

class VocabEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class VocabDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.toObject)

    def toObject(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = {
            key: value
            for key, value in d.items()
            }
            inst = class_(**args)
        else:
            inst = d
        
        return inst            

class Vocab:
    '''
    The Vocab object contains info about all the words
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''
    def __init__(self, vocabId, wordList):
        self.VocabId = vocabId
        self.WordList = wordList
        return

class VocabFile:
    def __init__(self, fileName = "D:\\Users\\achyu\\Source\\repos\\ia\\src\\VocabList.json"):
        self.FileName = fileName

    def ReadFile(self):
        fileExists = path.exists(self.FileName)
        if fileExists:
            with open(self.FileName, 'r') as infile:
                json_object = json.load(infile, cls=VocabDecoder)
        else:
            json_object = []

        return json_object

    def WriteFile(self, vocabList):
        with open(self.FileName, "w") as outfile:
            #question, what is the ^w for? --> read and write 
            json.dump(vocabList, outfile, cls=VocabEncoder)
        return

    def GetVocab(vocabId):
        vocabList = self.ReadFile()
        # find matching vocab

        vocab = "blah"
        return vocab

    def AddVocab(self, vocab):
        # read all vocab from file
        vocabList = self.ReadFile()
        # check if vocab already exists
        for v in vocabList:
            if v.VocabId == vocab.VocabId:
                raise VocabAlreadyExists()

        # append
        vocabList.append(vocab)
        print(vocabList)
        # write
        self.WriteFile(vocabList)
        return