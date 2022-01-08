from funcs import Vigenere64
from tkinter import *

intro = Tk()
intro.geometry("1200x675")
intro.minsize(1200, 675)
intro.maxsize(1200, 675)

vigImg = PhotoImage(file="Vigenere.jpg")
label = Label(master=intro,image=vigImg)
label.pack()

intro.mainloop()
