from tkinter import *
from funcs import Vigenere64

def SecondScreen(fileToConvert,option,window):
    DEFAULTCOLOR = "#FFFFFF"
    BUTTONCOLOR = "#00ACFF"

    screen2 = Frame(window,pady=50,background=DEFAULTCOLOR)
    screen2.pack()

    descriptionBox = Frame(screen2,background=DEFAULTCOLOR)
    descriptionBox.pack()
    descriptionTitle = Label(descriptionBox,text="File Description",font=("Times New Roman",24),fg="black",background=DEFAULTCOLOR)
    descriptionTitle.pack()
    





