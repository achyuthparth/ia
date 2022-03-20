from tkinter import *


def myClick():
    myLabel = Label(root,
        text = "Button Called")
    myLabel.pack


class Application(Tk):

    def __init__(self, *args, **kwargs):  
        Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = 'top', 
            fill = 'both', 
            expand = True)

        self.frame = {}
        self.frame[StartupFrame] = StartupFrame(container, self)
        self.frame[PracticeFrame] = PracticeFrame(container, self)
        self.frame[GameFrame] = GameFrame(container, self)

    def ShowFrame(self, frameTypeToShow):
        frame = self[frameTypeToShow]
        frame.tkraise()


class StartupFrame(Frame):
    def __init__(self, parent, application):
        this.Application = application
        Frame.__init__(self, parent)
        startFrame = LabelFrame(self, text = "Welcome")

        #defining buttons
        practiceButton = Button(startFrame, 
            text = "Practice", 
            command = application.ShowFrame(PracticeFrame)
            #to practice sets screen
            )

        enteringButton = Button(startFrame, 
            text = "Enter New Set", 
            command = application.ShowFrame(PracticeFrame)
            #to enter wordlist screen
            )

        progressButton = Button(startFrame, 
            text = "View Progress Report", 
            command = application.ShowFrame(PracticeFrame)
            #to progress report screen
            )

        startFrame.pack()
        practiceButton.pack()
        enteringButton.pack()
        progressButton.pack()

class PracticeFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        this.Application = application
        Frame.__init__(self, parent)
        practiceFrame = LabelFrame(self, text = "Practice Vocabulary")

        gameButton = Button(
            practiceFrame,
            text = "Start Practice",
            command = application.ShowFrame(GameFrame),
            )

        gameButton.pack()


        #setDrop = OptionMenu(
    # practiceFrame,
    #clicked,
    #insert the wordlists here
    #)


    #setDrop.pack()

class EnterWordlistFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        this.Application = application
        Frame.__init__(self, parent)
        enterFrame = LabelFrame(self, "Enter a new word list")

        submitWord = Button(
        enterFrame,
        text = "Submit",
        #command = enterWord.get()
        )
        #fix drop down
        #enterWord = Entry(
        #    enterFrame,
        #    width = 50,
        #    text = "Enter Word",
        #    )
       

class GameFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        this.Application = application
        Frame.__init__(self, parent)
        gameFrame = LabelFrame(self, "Practice Vocab")

        submitWord = Button(
        gameFrame,
        text = "Submit",
        command = fillBlank.get()
        )
        
        fillBlank = Entry(
            gameFrame,
            width = 30,
            text = "cual palabra?")

        vocabWord = Label(
            gameFrame,
            text = getVocab())


root.mainloop()
