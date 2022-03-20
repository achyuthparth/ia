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

        self.Frames = {}
        for F in (StartupFrame, PracticeFrame, EnterWordlistFrame, GameFrame):
            frame = F(container, self)
            self.Frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew") 

        self.ShowFrame(StartupFrame)

    def ShowFrame(self, frameTypeToShow):
        frame = self.Frames[frameTypeToShow]
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

class PracticeFrame(Frame):
    def __init__(self, parent, application):
        Frame.__init__(self, parent)
        self.Application = application
        uberLabelFrame = LabelFrame(self, text = "Practice Vocabulary")

        gameButton = Button(uberLabelFrame,
            text = "Start Practice",
            command = lambda: application.ShowFrame(GameFrame),)

        uberLabelFrame.pack()
        gameButton.pack()


        #setDrop = OptionMenu(
    # uberLabelFrame,
    #clicked,
    #insert the wordlists here
    #)


    #setDrop.pack()
class EnterWordlistFrame(Frame):
    def __init__(self, parent, application):
        Frame.__init__(self, parent)
        self.Application = application
        enterFrame = LabelFrame(self, text = "Enter a new word list")


        
        enterVocabID = Entry(enterFrame,
            width = 50)
        enterVocabID.insert(0, "Enter Vocab ID")

        enterVocab = Text(enterFrame,
                    width = 50)
        enterVocab.insert(0, "Enter Vocab, eg: cat, dog, etc...")

        vocab = [enterVocabID.get(), enterVocab.get()]

        submitWord = Button(enterFrame,
        text = "Submit",
        #command = LS.VocabFile.AddVocab(vocab)
        #command = enterWord.get()
        )


        #fix drop down

        #vLister = Label(enterFrame,
        #    text = enterWord.get())


        
        enterFrame.pack()   
        enterVocabID.pack()
        
        #vLister.pack()
        enterVocab.pack()
        submitWord.pack()


class GameFrame(Frame):
    def __init__(self, parent, application):
        self.Application = application
        Frame.__init__(self, parent)
        gameFrame = LabelFrame(self, text = "Practice Vocab")

        submitWord = Button(gameFrame,
        text = "Submit",
        command = lambda: fillBlank.get())
        
        fillBlank = Entry(gameFrame,
            width = 30,
            text = "cual palabra?")

        vocabWord = Label(gameFrame,
            text = "vocab comes here")



        gameFrame.pack()
        fillBlank.pack()
        vocabWord.pack()
        submitWord.pack()



root = Application()

root.mainloop()

