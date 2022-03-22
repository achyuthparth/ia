from tkinter import *
import LanguageServices as LS
import ActivityServices as AS
import TranslatorServices as TS
import FileServices as FS


def myClick():
    myLabel = Label(root,
        text = "Button Called")
    myLabel.pack


class Application(Tk):

    def __init__(self, *args, **kwargs):  
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side = 'top', 
            fill = 'both', 
            expand = True)

        self.SelectedVocabId = None


        self.Frames = {}
        for F in (StartupFrame, PracticeFrame, EnterWordlistFrame, GameFrame):
            frame = F(container, self)
            self.Frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew") 

        self.ShowFrame(StartupFrame)

        goHomeButton = Button(self,
            text = "Go Home",
            command = lambda: self.ShowFrame(StartupFrame))

        goHomeButton.pack()
    
    def ShowFrame(self, frameTypeToShow):
        frame = self.Frames[frameTypeToShow]
        frame.Reset()
        frame.tkraise()

 
class StartupFrame(Frame):
    def __init__(self, parent, application):
        self.Application = application
        Frame.__init__(self, parent)
        startFrame = LabelFrame(self, text = "Welcome")

        #defining buttons
        practiceButton = Button(startFrame, 
            text = "Practice", 
            command = lambda: application.ShowFrame(PracticeFrame)
            #to practice sets screen
            )

        enteringButton = Button(startFrame, 
            text = "Enter New Set", 
            command = lambda: application.ShowFrame(EnterWordlistFrame)
            #to enter wordlist screen
            )
        
        progressButton = Button(startFrame, 
            text = "View Progress Report", 
            command = lambda: application.ShowFrame(PracticeFrame)
            #to progress report screen
            )

        startFrame.pack()
        practiceButton.pack()
        enteringButton.pack()
        progressButton.pack()

    def Reset(self):
        print("in Startupframe reset function")
        return

class PracticeFrame(Frame):
    def __init__(self, parent, application):
        Frame.__init__(self, parent)
        self.Application = application
        self.Selection = StringVar()
        self.dropVocabIds = None
        self.uberLabelFrame = LabelFrame(self, text = "Practice Vocabulary")
        self.uberLabelFrame.pack()

        gameButton = Button(self.uberLabelFrame,
            text = "Start Practice",
            command = self.OnSelection)
        gameButton.pack()

    def PopulateDropDown(self):
        if not self.dropVocabIds is None:
            self.dropVocabIds.destroy()
            self.dropVocabIds = None

        vocabList = LS.VocabFile().GetVocabIds()
        if len(vocabList) > 0:
            self.Selection.set(vocabList[0])

        self.dropVocabIds = OptionMenu(self.uberLabelFrame,
            self.Selection,
            *vocabList)
        self.dropVocabIds.pack()
        
    def OnSelection(self):
        self.Application.SelectedVocabId = self.Selection.get()
        self.Application.ShowFrame(GameFrame)

    def Reset(self):
        print("in PracticeFrame reset function")
        self.PopulateDropDown()
        return


class EnterWordlistFrame(Frame):
    def __init__(self, parent, application):
        Frame.__init__(self, parent)
        self.Application = application
        enterFrame = LabelFrame(self, text = "Enter a new word list")

        self.enterVocabID = Entry(enterFrame, width = 50)
        self.enterVocabID.insert(0, "Id_")

        self.enterVocab = Text(enterFrame,
                    height = 15,
                    width = 50)
        
        submitWord = Button(enterFrame,
            text = "Submit",
            command = self.OnSubmit)

        enterFrame.pack()   
        self.enterVocabID.pack()
        self.enterVocab.pack()
        submitWord.pack()

    def OnSubmit(self):
        vocabId = self.enterVocabID.get()
        wordsFull = self.enterVocab.get('1.0', 'end')
        print(vocabId + " : " + wordsFull)

        wordList = list(filter(None, wordsFull.split("\n")))
        vocab = LS.Vocab(vocabId, wordList)
        vocabFile = LS.VocabFile()
        # TODO: error handling, what if vocab already exists?
        vocabFile.AddVocab(vocab)

        # TODO: add confirmation message
        
    def Reset(self):
        print("in EnterWordlistFrame reset function")
        return

class GameFrame(Frame):
    def __init__(self, parent, application):
        self.Application = application
        Frame.__init__(self, parent)
        gameFrame = LabelFrame(self, text = "Practice Vocab")
        self.dictionary = TS.TranslateService().GetDictionary()

        self.vocab = None

        self.vocabWordLabel = Label(gameFrame,
            text = "<none>")

        self.correctAnswerLabel = Label(gameFrame,
            text = "<none>")

        self.checkWordButton = Button(gameFrame,
            text  = "Check",
            command = lambda: self.checkWord)

        self.nextWordButton = Button(gameFrame,
            text = "Next",
            command = lambda: self.nextWord)

        self.inputAnswer = Entry(gameFrame,
            width = 30,)


        gameFrame.pack()
        self.vocabWordLabel.pack()
        self.inputAnswer.pack()
        self.correctAnswerLabel.pack()
        self.checkWordButton.pack()
        self.nextWordButton.pack()


    def ShowWord():

        #remove current words
        self.vocabWordLabel.pack_forget()
        self.correctAnswerLabel.pack_forget()

        # update widget values
        word = self.vocab.WordList[self.i]
        translatedWord = self.dictionary[word]
        self.vocabWordLabel.set(word)
        self.correctAnswerLabel.set(translatedWord)
        # show or hide the widgets

        self.vocabWordLabel.pack()
        return

    def checkWord():
        word = self.vocab.WordList[self.i]
        self.correctAnswer = self.dictionary[word]

        self.correctAnswerLabel.pack()
        return

    def nextWord(self):
        self.i += 1
        # todo: fix this
        countLength = 0
        if self.i > countLength:
            self.nextWordButton.pack_forget()
            return

        ShowWord()
        return

    def Reset(self):
        print("in GameFrame reset function")
        # read selected vocab id and use the word list from it
        self.vocab = LS.VocabFile().GetVocab(self.Application.SelectedVocabId)
        self.i = 0
        self.correctCount = 0
        self.wrongCount = 0
        ShowWord()
        return


root = Application()

root.mainloop()

