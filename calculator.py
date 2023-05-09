#Necessarry import for creating a GUI.
from tkinter import *

#Creating a GUI windowm, naming it and adding photoimage.
window = Tk()
window.title("Calculator")
icon = PhotoImage(file="calculator.png")
window.iconphoto(True, icon)

#Creating a input space inside window.
input = Entry(window, width=55, borderwidth=5)
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Defining button click functions.
def buttonClick(number):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))

def buttonC():
    input.delete(0, END)

def buttonIsEqual():
    operation = input.get()
    input.delete(0,END)
    input.insert(0, str(eval(operation)))
        
#Creating all the needed buttons.
buttonZero = Button(window,text="0", padx=40, pady=20, command= lambda: buttonClick(0), activeforeground='black', activebackground='white')
buttonOne = Button(window,text="1", padx=40, pady=20, command= lambda: buttonClick(1), activeforeground='black', activebackground='white')
buttonTwo = Button(window,text="2", padx=40, pady=20, command= lambda: buttonClick(2), activeforeground='black', activebackground='white')
buttonThree = Button(window,text="3", padx=40, pady=20, command= lambda: buttonClick(3), activeforeground='black', activebackground='white')
buttonFour = Button(window,text="4", padx=40, pady=20, command= lambda: buttonClick(4), activeforeground='black', activebackground='white')
buttonFive = Button(window,text="5", padx=40, pady=20, command= lambda: buttonClick(5), activeforeground='black', activebackground='white')
buttonSix = Button(window,text="6", padx=40, pady=20, command= lambda: buttonClick(6), activeforeground='black', activebackground='white')
buttonSeven = Button(window,text="7", padx=40, pady=20, command= lambda: buttonClick(7), activeforeground='black', activebackground='white')
buttonEight = Button(window,text="8", padx=40, pady=20, command= lambda: buttonClick(8), activeforeground='black', activebackground='white')
buttonNine = Button(window,text="9", padx=40, pady=20, command= lambda: buttonClick(9), activeforeground='black', activebackground='white')
buttonPlus = Button(window, text="+", padx=40, pady=20, command= lambda: buttonClick("+"), activeforeground='black', activebackground='white')
buttonMinus = Button(window,text="-",  padx=40, pady=20, command= lambda: buttonClick("-"), activeforeground='black', activebackground='white')
buttonMultiply = Button(window,text="*", padx=40, pady=20, command= lambda: buttonClick("*"), activeforeground='black', activebackground='white')
buttonDevide = Button(window,text="/", padx=40, pady=20, command= lambda: buttonClick("/"), activeforeground='black', activebackground='white')
buttonDot = Button(window, text=".", padx=41, pady=20, command=lambda: buttonClick("."), activeforeground='black', activebackground='white')
buttonClear = Button(window,text="C", padx=39, pady=20, command=buttonC, activeforeground='black',activebackground='white')
buttonEquals = Button(window, text="=", padx=139, pady=20,relief=SUNKEN , command=buttonIsEqual, activeforeground='black', activebackground='white')
buttonCalculatorPic = Button(window, image=icon, padx=40, pady=20)

#Placing the buttons inside the window with grid function.
buttonOne.grid(row=3, column=0)
buttonTwo.grid(row=3, column=1)
buttonThree.grid(row=3, column=2)
buttonFour.grid(row=2, column=0)
buttonFive.grid(row=2, column=1)
buttonSix.grid(row=2, column=2)
buttonSeven.grid(row=1, column=0)
buttonEight.grid(row=1, column=1)
buttonNine.grid(row=1, column=2)
buttonZero.grid(row=4, column=0)
buttonPlus.grid(row=4, column=3)
buttonMinus.grid(row=3, column=3)
buttonMultiply.grid(row=2, column=3)
buttonDevide.grid(row=1, column=3)
buttonClear.grid(row=4, column=2)
buttonDot.grid(row=4, column=1)
buttonEquals.grid(row=5 ,column=1,columnspan=3)
buttonCalculatorPic.grid(row=5, column=0)

#Window loop commant for keeping the app going.
window.mainloop()