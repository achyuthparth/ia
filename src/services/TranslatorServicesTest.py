from TranslatorServices import *

def TestTranslator():
	ts = TranslateService()
	wordList = [
		"cat",
		"apple",
		"dog",
		"winter",
		"dogs",
		"cats",
		]
	ts.Translate(wordList)


TestTranslator()