from LanguageServices import *


def TestVocabAdd():
    vocab = Vocab("Test 1", ["cat", "bat"])
    vocabFile = VocabFile()
    vocabFile.AddVocab(vocab)

def TestGetVocab():
    file = VocabFile()
    vocab = file.GetVocab("Test 1")
    return

#TestVocabAdd()
TestGetVocab()

