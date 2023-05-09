#Importing tkinter for creating GUI and strftime for current time displaying.
from tkinter import *
from time import strftime

#Creating gui window and setting up configurations.
window = Tk()
window.geometry("300x300")
window.title("Digital Clock")
window.config(background="blue")

#Adding icon image.
icon = PhotoImage(file="clock.png")
window.iconphoto(True, icon)

#Setting up label for current time.
label = Label(text="Current Time", font=('areal', 30, 'bold'), foreground= 'white', background= 'blue')
label.pack()

#Defining time function.
def time():
    string = strftime("%H:%M:%S")
    f1.config(text= string)
    f1.after(1000, time)

#Creating frame for positioning of time.
frame = Frame(window, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#Adding time into frame.
f1 = Label(frame, font=("arial",50,'bold'), foreground='white', background='blue')
f1.pack()

#Calling functions.
time()
window.mainloop()