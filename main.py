from os import linesep
from tkinter.font import BOLD, ITALIC
from funcs import Vigenere64
from tkinter import *
from tkinter import filedialog

DEFAULTCOLOR = "#FFFFFF" #color to be applied in all backgrounds
BUTTONCOLOR = "#00ACFF"

def encryptAction():
    x = filedialog.askopenfile()
    print(str(x.read()))

def decryptAction():
    print("button pressed aaa")



intro = Tk()
intro.geometry("1200x675")
intro.minsize(1200, 675)
intro.maxsize(1200, 675)
intro.title("FileCrypto")
intro.config(background=DEFAULTCOLOR)
icon = PhotoImage(file="icon.png")
intro.iconphoto(TRUE,icon)

vigImg = PhotoImage(file="Vigenere.png")

screen = Frame(intro,pady=50,background=DEFAULTCOLOR)
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




intro.mainloop()
