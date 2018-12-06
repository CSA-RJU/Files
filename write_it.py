from tkinter import * #imports
from tkinter import ttk
import glob

root = Tk()
def read(): #Reads the file and prints it to the message box.
    try:
        if str(optvar.get) == "": #This escentially means it will always fail.
            mesM.config(text="Please select a file to read!")
        else: #This will trigger anytime that a file is selected.
            opener = open(str(optvar.get()),'r')
            read = opener.read() 
            mesM.configure(text=read)
            opener.close
    except(FileNotFoundError): #This will only trigger if the "if" function fails, which it always does unless there's a selected file, and if it doesn't it still does it's job!
        mesM.config(text="Please select a file to read!")

def write(*args): #Opens a bug report toplevel.
    global notT
    EX = Toplevel(root)
    notL=Label(EX, text="File content:")  # Creates a label that says what's in the ".
    notL.grid(column=10, row=9, columnspan=20, sticky="NSEW")
    notT=Text(EX, width=5, height=5) #This is where to write the bug.
    notT.grid(column=10, row=10, columnspan=20, sticky="NSEW")
    canB=ttk.Button(EX, text="Quit", command=quit)  # Creates a "Quit" button.
    canB.grid(column=10, row=20, sticky="NSEW")
    subB=ttk.Button(EX, text="Submit", command=write2)  # Creates a "Submit" button.
    subB.grid(column=20, row=20, sticky="NSEW")
    EX.grid_columnconfigure(10, weight=1)
    EX.grid_columnconfigure(20, weight=1)
    EX.grid_rowconfigure(9, weight=1) 
    EX.grid_rowconfigure(10, weight=1)
    EX.grid_rowconfigure(20, weight=1)

def write2(): #Reads the file and prints it to the message box.
    try:
        if str(opt2var.get) == "": #This escentially means it will always fail.
            mesM.config(text="Please select a file to write to!")
        else: #This will trigger anytime that a file is selected.
            try:
                opener = open(str(opt2var.get()),'w')
                opener.write(str(notT.get(1.0, END)))
                opener.close
                mesM.config(text="File save success!")
            except(OSError):
                mesM.config(text="File name invalid!")
    except(FileNotFoundError): #This will only trigger if the "if" function fails, which it always does unless there's a selected file, and if it doesn't it still does it's job!
        mesM.config(text="Please select a file to write!")

optvar = StringVar()
option = ttk.Combobox(root, text="File to read", textvariable = optvar, state="readonly", width=15)
option.set("File name")
option.grid(row=10, column=10, sticky="NSEW")

opt2var = StringVar()
option2 = ttk.Combobox(root, text="File name", textvariable = opt2var, width=15)
option2.set("File name")
option2.grid(row=10, column=20, sticky="NSEW")

ReaB = Button(root, text='Read', width=15, command=read)
ReaB.grid(row=20, column=10, sticky="NSEW")

wriB = Button(root, text='write', width=15, command=write)
wriB.grid(row=20, column=20, sticky="NSEW")

mesM = Message(root, text='\nThis is where the contents of the file will appear!\n', relief="groove")
mesM.grid(row=30, column=10, columnspan=20, sticky="NSEW")
#mesSB = ttk.Scrollbar(root, orient=VERTICAL, command=mesM.yview)
#mesSB.grid(row=10, column=11, sticky="NSEW")
#mesM['yscrollcommand']=couSB.set

ui = ["user_input"]
val_list = []
val_list2 = []
for val in glob.glob("*.txt"):
    val_list.append(val) 
#for val2 in glob.glob("*"):
#    val_list2.append(val2)
option["values"] = val_list + val_list2
option2["values"] = ui + val_list + val_list2 
    

root.grid_columnconfigure(10,weight=1)
root.grid_columnconfigure(20,weight=1)
root.grid_rowconfigure(30,weight=1)

root.title("File Checker") #Makes the title what is in the "s.
root.mainloop()
root.destroy()
