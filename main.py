from os import linesep
from tkinter.font import BOLD, ITALIC
from tkinter import *
from tkinter import filedialog, messagebox
import secondScreen

DEFAULTCOLOR = "#FFFFFF" #color to be applied in all backgrounds
BUTTONCOLOR = "#00ACFF" #color to be applied in all buttons

def encryptAction():
    fileName = filedialog.askopenfilename()
    try:
        fileToConvert = open(fileName,mode="rb")
        screen.destroy()
        secondScreen.SecondScreen(fileToConvert,fileName,"encrypt",window)
    except Exception:
        messagebox.showinfo("Error","Error, file not found or unable to process")


def decryptAction():
    fileName = filedialog.askopenfilename()
    try:
        fileToConvert = open(fileName,mode="rb")
        screen.destroy()
        secondScreen.SecondScreen(fileToConvert,fileName,"decrypt",window)
    except Exception:
        messagebox.showinfo("Error","Error, file not found or unable to process")

window = Tk()
window.geometry("960x600")
window.minsize(960, 600)
window.maxsize(960, 600)
window.title("FileCrypto")
window.config(background=DEFAULTCOLOR)
icon = PhotoImage(file="icon.png")
window.iconphoto(TRUE,icon)

vigImg = PhotoImage(file="Vigenere.png")

screen = Frame(window,pady=50,background=DEFAULTCOLOR)
screen.pack()

header = Frame(screen,background=DEFAULTCOLOR)
header.pack()

label = Label(header,image=vigImg,background=DEFAULTCOLOR)
title = Label(header,text="FileCrypto",font=("Times New Roman",48,ITALIC),fg="red",padx=75,background=DEFAULTCOLOR)
label.pack(side=LEFT)
title.pack(side=RIGHT)

descriptionBox = Frame(screen,pady=35,background=DEFAULTCOLOR)
descriptionBox.pack()

descriptionText = Label( descriptionBox,text="Python3 GUI application to encrypt files using \nthe Vingenère Cipher",
                        font=("Calibri",20),fg="black",background=DEFAULTCOLOR,justify=LEFT)
descriptionText.pack()

actionButtons = Frame(screen,background=DEFAULTCOLOR,pady=15)
actionButtons.pack()

encrypt = Button(actionButtons,background=BUTTONCOLOR,text="encrypt file",font=("Calibri",14,BOLD),
                 activebackground="#005A86",bd=0,relief=RIDGE,command=encryptAction)
encrypt.pack(side=TOP)
orText = Label(actionButtons,text="or",font=("Calibri",14),fg="#CBCBC6",background=DEFAULTCOLOR,justify=CENTER,pady=10)
orText.pack()
decrypt = Button(actionButtons,background=BUTTONCOLOR,text="decrypt file",font=("Calibri",14,BOLD),
                 activebackground="#005A86",bd=0,relief=RIDGE,command=decryptAction)
decrypt.pack(side=BOTTOM)

window.mainloop()
