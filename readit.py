from tkinter import * #imports
from tkinter import ttk
import glob
root = Tk()
def read(): #Reads the file and prints it to the message box.
    try:
        if str(optvar.get) == "": #This escentially means it will always fail.
            mesM.config(text="Please select a file!")
        else: #This will trigger anytime that a file is selected.
            opener = open(str(optvar.get()),'r')
            read = opener.read() 
            mesM.configure(text=read)
    except(FileNotFoundError): #This will only trigger if the "if" function fails, which it always does unless there's a selected file, and if it doesn't it still does it's job!
        mesM.config(text="Please select a file!")

mesM = Message(root, text='\nThis is where the contents of the file will appear!\n', borderwidth=2, relief="groove")
mesM.grid(row=10, column=10, rowspan=20)
#mesSB = ttk.Scrollbar(root, orient=VERTICAL, command=mesM.yview)
#mesSB.grid(row=10, column=11, sticky="NSEW")
#mesM['yscrollcommand']=couSB.set

optvar = StringVar()
option = ttk.Combobox(root,text='', textvariable = optvar, state="readonly", width=15)
option['values'] = ('')
option.grid(row=10, column=20)

ReaB = Button(root, text='Read', command=read)
ReaB.grid(row=20, column=20)

val_list = []
for val in glob.glob('*.txt'):
    val_list.append(val)
option['values'] = val_list
