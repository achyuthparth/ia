from tkinter import *

root = Tk()

top = Toplevel()





def myClick():
    myLabel = Label(root,
        text = "Button Called"
        )
    myLabel.pack




#defining buttons
practiceButton = Button(root, 
    text = "Practice", 
    command = myClick
    #to practice sets screen
    )

enteringButton = Button(root, 
    text = "Enter New Set", 
    command = myClick
    #to enter wordlist screen
    )

progressButton = Button(root, 
    text = "View Progress Report", 
    command = myClick
    #to progress report screen
    )

#initialize buttons

practiceButton.pack()
enteringButton.pack()
progressButton.pack()



root.mainloop()