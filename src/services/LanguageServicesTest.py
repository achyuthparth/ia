from LanguageServices import *


def TestVocabAdd():
    vocab = Vocab("Test 1", ["cat", "bat"])
    vocabFile = VocabFile()
    vocabFile.AddVocab(vocab)

TestVocabAdd()
