
"""LanguageServices.py: This file has classes and methods for Vocabulary management."""

__author__      = "Achyuthaa Parthasarathy"

import json
from pathlib import Path

class VocabAlreadyExists(Exception): pass


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
    def __init__(self, fileName = "VocabList.json"):
        self.FileName = fileName

    def ReadFile(self):
        ''' read the content of the file
        '''

        fileExists = Path.exists(self.FileName)
        if fileExists:
            with open(self.FileName, 'r') as infile:
                json_object = json.load(infile)
        else:
            json_object = []

        return json_object

    def WriteFile(self, vocabList):
        with open(self.FileName, "w") as outfile:
            #question, what is the ^w for? --> read and write 
            json.dump(vocabList, outfile)
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