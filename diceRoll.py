#Importing modules for generating a random integer and tkinter for GUI creating.
import random
from tkinter import *

#Setting up gui window and setting up window configurations.
window = Tk()
window.geometry("420x420")
window.title("Dice Roll")
window.config(background="#FF5733")

#Adding a frame in the middle of the window for displaying dice pictures.
frame = Frame(window, width=200, height=200,background="#FF5733")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#Converting our images into photo images.
icon = PhotoImage(file = 'dice.png' )
diceIcon = PhotoImage(file = 'diceIcon.png')
numberSix = PhotoImage(file = 'diceSix.png')
numberFive = PhotoImage(file = 'diceFive.png')
numberFour = PhotoImage(file = 'diceFour.png')
numberThree = PhotoImage(file = 'diceThree.png')
numberTwo = PhotoImage(file = 'diceTwo.png')
numberOne = PhotoImage(file = 'diceOne.png')

#Setting icon as and window icon photo.
window.iconphoto(True, icon)

#Function for randomly choosing the the number(picture of dice number).
def diceRoll():
    deleteFrame()
    dice = [numberOne, numberTwo, numberThree, numberFour, numberFive, numberSix]
    rollIt = Label(frame,image =random.choice(dice))
    rollIt.pack()

#Function for deleting previous widget after displaying and pressing roll button.    
def deleteFrame():
    for i in frame.winfo_children():
        Widget.destroy(i)
    frame.pack_forget()

#Setting title with its settings.        
label = Label(window,text="Welcome to random dice roll toss!",
              font=('Arial',14,'bold'),
              fg='white',
              bg='#FF5733',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=5,
              )
label.pack()

#Creating a button with its settings and functions.
button1 = Button(window,
                text="roll the dice",
                command=diceRoll,
                font=('Arial',14),
                fg = 'white',
                bg='#FF5733',
                activeforeground='white',
                activebackground= '#FF5733',
)

#Positioning the button.
button1.pack(side= 'bottom')

#setting window to be an infinite loop.
window.mainloop()
