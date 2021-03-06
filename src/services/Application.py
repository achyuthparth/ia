from datetime import datetime
from tkinter import *
from tkinter import ttk
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
        for F in (StartupFrame, PracticeFrame, EnterWordlistFrame, GameFrame, ProgressFrame):
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
            command = lambda: application.ShowFrame(ProgressFrame)
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
        TS.TranslateService().Translate(wordList)
        vocab = LS.Vocab(vocabId, wordList)
        vocabFile = LS.VocabFile()
        # TODO: error handling, what if vocab already exists?
        vocabFile.AddVocab(vocab)

        # TODO: add confirmation message
        

        #go back to starting frame
        application.ShowFrame(StartupFrame)
    def Reset(self):
        print("in EnterWordlistFrame reset function")
        return

class GameFrame(Frame):
    def __init__(self, parent, application):
        self.Application = application
        Frame.__init__(self, parent)
        gameFrame = LabelFrame(self, text = "Practice Vocab")

        self.dictionary = TS.TranslateService().GetDictionary()
        self.correctAnswerVar = StringVar()
        self.vocabWordVar = StringVar()
        self.vocab = None

        self.doneButton = Button(gameFrame,
            text = "Done",
            command = self.OnDone)

        self.vocabWordLabel = Label(gameFrame,
            textvariable = self.vocabWordVar)

        self.correctAnswerLabel = Label(gameFrame,
            textvariable = self.correctAnswerVar)

        self.checkWordButton = Button(gameFrame,
            text  = "Check",
            command = self.checkWord)

        self.nextWordButton = Button(gameFrame,
            text = "Next",
            command = self.nextWord)

        self.inputAnswer = Entry(gameFrame,
            width = 30,)


        gameFrame.pack()
        self.vocabWordLabel.pack()
        self.inputAnswer.pack()
        self.correctAnswerLabel.pack()
        self.checkWordButton.pack()
        self.nextWordButton.pack()
        self.doneButton.pack()


    def ShowWord(self):

        #remove current words
        self.vocabWordLabel.pack_forget()
        self.correctAnswerLabel.pack_forget()

        # update widget values
        word = self.vocab.WordList[self.i]
        translatedWord = self.dictionary[word]
        self.vocabWordVar.set(word)
        self.correctAnswerVar.set(translatedWord)
        # show or hide the widgets

        self.vocabWordLabel.pack()
        countLength = len(self.vocab.WordList)
        if self.i >= countLength-1:
            self.nextWordButton.pack_forget()
            
        return

    def OnDone(self):
        # save activity score
        activity = AS.Activity(
            self.Application.SelectedVocabId,
            datetime.now(),
            self.correctCount,
            self.wrongCount)
        AS.ActivityFile().AddActivity(activity)
        sself.Application.ShowFrame(ProgressFrame)
        return

    def checkWord(self):
        word = self.vocab.WordList[self.i]
        self.correctAnswer = self.dictionary[word]
        if self.correctAnswer == self.inputAnswer.get():
            self.correctCount += 1
        else:
            self.wrongCount += 1

        self.correctAnswerLabel.pack()
        return

    def nextWord(self):
        self.i += 1
        self.ShowWord()
        return

    def Reset(self):
        print("in GameFrame reset function")
        # read selected vocab id and use the word list from it
        self.vocab = LS.VocabFile().GetVocab(self.Application.SelectedVocabId)
        self.i = 0
        self.correctCount = 0
        self.wrongCount = 0
        self.correctAnswerVar.set("")
        self.vocabWordVar.set("")
        self.ShowWord()
        return



class ProgressFrame(Frame):
    def __init__(self, parent, application):
        self.Application = application
        Frame.__init__(self, parent)
        progressFrame = LabelFrame(self, text = "Activity Report")

        self.activityGrid = None


    def Reset(self):
        if not self.activityGrid is None:
            self.activityGrid.destroy()
            self.activityGrid = None
            
        self.activityGrid = ttk.Treeview(self)
        self.activityGrid['columns'] = ('Vocab List', 'Date and Time', 'Correct Responses', 'Incorrect Responses')
        self.activityGrid.column("#0", width = 0,
                                 stretch = NO)
        self.activityGrid.column("Vocab List", anchor=CENTER)
        self.activityGrid.column("Date and Time", anchor = CENTER)
        self.activityGrid.column("Correct Responses", anchor = CENTER)
        self.activityGrid.column("Incorrect Responses", anchor = CENTER)

        self.activityGrid.heading("#0", text = "", anchor = CENTER)
        self.activityGrid.heading("Vocab List", text = "Vocab List", anchor = CENTER)
        self.activityGrid.heading("Date and Time", text = "Date and Time", anchor = CENTER)
        self.activityGrid.heading("Correct Responses", text = "Correct Responses", anchor = CENTER)
        self.activityGrid.heading("Incorrect Responses", text = "Incorrect Responses", anchor = CENTER)

        activityList = AS.ActivityFile().ReadFile()
        j = 0
        for a in activityList:
            self.activityGrid.insert(parent='',
                index='end',
                iid=j,text='',
                values = (a.VocabId, 
                          a.DateTime.__str__(), 
                          a.NumCorrect, 
                          a.NumWrong))
            j += 1
        self.activityGrid.pack()

root = Application()

root.mainloop()


# TODO: Progress report frame
# TODO: Wire progress report frame up to Game Frame and Start Frame
# TODO: Class diagrams
# TODO: Ordering of widgets in GameFrame