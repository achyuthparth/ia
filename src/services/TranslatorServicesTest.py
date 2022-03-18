from TranslatorServices import *

def TestTranslator():
	ts = TranslateService()
	wordList = [
		"cat",
		"apple",
		"dog",
		"winter",
		]
	ts.Translate(wordList)


TestTranslator()