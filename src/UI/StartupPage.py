from tkinter import *

def myClick():
    myLabel = Label(root,
        text = "Button Called"
        )
    myLabel.pack


root = Tk()
#root.title = "This is root's title"

startFrame = LabelFrame(
    root,
    text = "Welcome",
    #padx = 1920,
    #pady = 1080
    )

#startFrame = root

#defining buttons
practiceButton = Button(
    startFrame, 
    text = "Practice", 
    command = myClick
    #to practice sets screen
    )

enteringButton = Button(
    startFrame, 
    text = "Enter New Set", 
    command = myClick
    #to enter wordlist screen
    )

progressButton = Button(
    startFrame, 
    text = "View Progress Report", 
    command = myClick
    #to progress report screen
    )

#initialize buttons

startFrame.pack()
practiceButton.pack()
enteringButton.pack()
progressButton.pack()


practiceFrame = LabelFrame(
    root,
    text = "Practice",
    padx = 1920,
    pady = 1080
    )

gameButton = Button(
    practiceFrame,
    text = "Start",
    command = myClick,
    )

#setDrop = OptionMenu(
    # practiceFrame,
    #clicked,
    #insert the wordlists here
    #)


    #setDrop.pack()
gameButton.pack()

enterFrame = LabelFrame(
    root,
    text = "Enter New Wordlist",
    padx = 1920,
    pady = 1080
    )

submitWord = Button(
    enterFrame,
    text = "Submit",
    command = myClick
    )

enterWord = Entry(
    enterFrame,
    width = 50,
    text = "Enter Word",
    )

choosGame = LabelFrame(
    root,
    text = "Choose Wordlist",
    padx = 1920,
    pady = 1080
    )

enEs = Button(
    choosGame,
    text = "English to Spanish",
    command = myClick
    )

esEn = Button(
    choosGame,
    text = "Spanish to English",
    command = myClick
    )

gameFrame = LabelFrame(
    root,
    text = "Fill in the blanks with the appropriate word",
    padx = 1920,
    pady = 1080
    )

fillBlank = Entry(
    gameFrame,
    width = 30,
    text = "cual palabra?")

submitEntry = Button(
    gameFrame,
    text = "submit answers",
    command = myClick
    )



root.mainloop()
