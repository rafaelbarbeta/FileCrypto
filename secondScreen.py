from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
from tkinter.font import ITALIC, BOLD
from funcs import Vigenere64
from os.path import getsize, basename

logs_text = "logs are shown here"

def setInfo(pathFileName):
    fileInfo = ["","",""]
    counter = 0.0
    fileInfo[0] = basename(pathFileName)
    fileInfo[1] = int(getsize(pathFileName))
    while fileInfo[1]/1024 > 1:
        fileInfo[1] = fileInfo[1]/1024
        counter = counter + 1
    if counter == 0:
        fileInfo[1] = str(fileInfo[1]) + "B"
    elif counter == 1:
        fileInfo[1] = str(fileInfo[1]) + "KB"
    elif counter == 2:
        fileInfo[1] = str(fileInfo[1]) + "MB"
    elif counter == 3:
        fileInfo[1] = str(fileInfo[1]) + "GB"
    else:
        fileInfo[1] = "error"
    
    indexPoint = str(fileInfo[0]).find(".")
    extension = str(fileInfo[0])[indexPoint::]

    if extension in {".png", ".jpeg", ".jpg", ".gif", ".tif", ".svg", ".bmp", ".ico", ".webp"}:
        fileInfo[2] = "Image File"
    elif extension in {".mp4", ".mov", ".wmv", ".flv", ".avi", ".mkv"}:
        fileInfo[2] = "Video File"
    elif extension in {".aif", ".mp3", ".mdi", ".ogg", ".wav", ".wma", ".wpl"}:
        fileInfo[2] = "Audio File"
    elif extension in {".7z", ".rar", ".pkg", ".deb", ".tar", ".tar.gz", ".z", ".gz", ".zip"}:
        fileInfo[2] = "Compressed File"
    elif extension in {".apk", ".bat", ".exe", ".jar", ".msi"}:
        fileInfo[2] = "Executable File"
    elif extension in {".key", ".odp", ".pps", ".ppt", ".pptx"}:
        fileInfo[2] = "Presentation File"
    elif extension in {".c", ".py", ".class", ".cpp", ".cs", ".h", ".java", ".sh", ".vb", ".php", ".swift"}:
        fileInfo[2] = "Programming Related File"
    elif extension in {".ods", ".xls", ".xlsm", ".xlsx"}:
        fileInfo[2] = "SpreadSheet File"
    elif extension in {".txt", ".pdf", ".md", ".doc", ".docx", ".odt"}:
        fileInfo[2] = "Text File"
    else:
        fileInfo[2] = "Unknown File Type"
    
    return fileInfo

def run(fileToConvert,pathFileName,option,key,window,bar):
    answer = messagebox.askquestion("Warning","Are you sure you want to "+option+" this file?")
    if answer == "no":
        return 0
    bin_to_convert = fileToConvert.read()
    bar["value"] += 20
    window.update_idletasks()
    fileToConvert.close()
    vigenere = Vigenere64(bin_to_convert,key)
    if option == "encrypt":
        vigenere.byte_to_b64()
        bar["value"] += 20
        window.update_idletasks()
        vigenere.encrypt()
        bar["value"] += 20
        window.update_idletasks()
        bin_converted = vigenere.b64_to_byte()
        bar["value"] += 20
        window.update_idletasks()
    else:
        vigenere.byte_to_b64()
        bar["value"] += 20
        window.update_idletasks()
        vigenere.decrypt()
        bar["value"] += 20
        window.update_idletasks()
        bin_converted = vigenere.b64_to_byte()
        bar["value"] += 20
        window.update_idletasks()
    with open(pathFileName,"wb") as file_converted:
        file_converted.write(bin_converted)
    bar["value"] += 20
    window.update_idletasks()
    messagebox.showinfo("Operation Successful","File has been "+option+"ed")
    window.destroy()

def SecondScreen(fileToConvert,pathFileName,option,window):
    DEFAULTCOLOR = "#FFFFFF"
    BUTTONCOLOR = "#00ACFF"
    fileInfo = ["","",""]
    fileInfo = setInfo(pathFileName)
    infoText = "Name: "+fileInfo[0]+"\n"+"Path: "+pathFileName+"\n"+"Size: "+fileInfo[1]+"\n"+"Type: "+fileInfo[2]

    screen2 = Frame(window,pady=50,background=DEFAULTCOLOR)
    screen2.pack()

    descriptionBox = Frame(screen2,background=DEFAULTCOLOR)
    descriptionBox.pack()
    descriptionTitle = Label(descriptionBox,text="File Description",font=("Times New Roman",24),fg="black",background=DEFAULTCOLOR)
    descriptionTitle.pack()
    infoBox = Label(descriptionBox,text=infoText,font=("Times New Roman",18),fg="black",background=DEFAULTCOLOR,pady=35,justify=LEFT,wraplength=400)
    infoBox.pack()

    passwordBox = Frame(screen2,background=DEFAULTCOLOR)
    passwordBox.pack()

    pleasePassword = Label(passwordBox,text="Please type the password to encrypt/decrypt:",font=("Times New Roman",16,ITALIC),fg="grey",background=DEFAULTCOLOR)
    pleasePassword.pack(side=TOP)
    entry = Entry(passwordBox,background=DEFAULTCOLOR,fg="black",width=30,bd=3,relief=RIDGE,font=("Times New Roman",14))
    entry.pack(side=BOTTOM,pady=15)

    ProgressBox = Frame(screen2,background=DEFAULTCOLOR)
    ProgressBox.pack(pady=35)

    logs = Label(ProgressBox,background=DEFAULTCOLOR,text=logs_text,font=("Calibri",10),fg="grey")
    logs.grid(column=8,row=0,columnspan=8)

    style = Style()
    style.configure("TProgressbar",thickness=25) #changes the progress bar style thickness
    bar = Progressbar(ProgressBox,length=400)
    bar.grid(column=0,row=1,columnspan=20)

    runButton = Button(ProgressBox,background=BUTTONCOLOR,text=option+"!",font=("Calibri",12,BOLD),
                 activebackground="#005A86",bd=0,relief=RIDGE,command=lambda:run(fileToConvert,pathFileName,option,entry.get(),window,bar))
    runButton.grid(column=21,row=1,padx=25)