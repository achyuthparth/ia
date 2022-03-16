from LanguageServices import *


def TestVocabAdd():
    vocab = Vocab("Test2", ["rat", "sat"])
    vocabFile = VocabFile()
    vocabFile.AddVocab(vocab)
    vocab = Vocab("Test3", ["mat", "lat"])
    vocabFile.AddVocab(vocab)

def TestGetVocab():
    file = VocabFile()
    vocab = file.GetVocab("Test 1")
    return

TestVocabAdd()
TestGetVocab()

