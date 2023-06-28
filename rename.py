import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, simpledialog

t = Tk()

t.geometry("700x700")
t.title("File Renamer")

def fileRenamer():
    numberOfFiles = simpledialog.askinteger("File Renamer", "How many files?")
    for i in range(numberOfFiles):
            file_path = filedialog.askopenfilename()
            file_list.append(file_path)
    
    def displayFiles():
        for file_path in file_list:
            file_listbox.insert(END, file_path)
    
    def Rename():
        fileRename = simpledialog.askstring("File Rename", "Rename as?")
        for i in range(numberOfFiles):
            file_extension = os.path.splitext(file_path)[1]
            new_file_name = f"{fileRename}_{i}{file_extension}"
            os.rename(file_list[i], new_file_name)
            updatedFiles.append(new_file_name)

    def showUpdatedFiles():
     file_listbox.delete(0, END)
     for item in updatedFiles:
          file_listbox.insert(END, item)

    def openFileLocation(event):
     index = file_listbox.curselection()
     if index:
          directory = os.path.dirname(file_list[i])
          os.system('open %s' % directory)
    
    file_listbox.bind("<Button-1>", openFileLocation)
    displayFiles()
    Rename()    
    showUpdatedFiles()




    

file_reversal_button = tk.Button(text = "File Renamer", command = fileRenamer)
file_reversal_button.pack()
file_listbox = Listbox(t)
file_listbox.pack(fill="x")

#Store text for string reversal
reversal_text = tk.StringVar()
def stringReversal():
     input_text = stringReversalInput.get()
     reversed_text = input_text[::-1]
     stringReversalInput.delete(0, END)
     stringReversalInput.insert(0, reversed_text)


stringReversalLabel = tk.Label(t, text="String Reversal")
stringReversalLabel.pack()
stringReversalInput = tk.Entry(textvariable = reversal_text)
stringReversalInput.pack()
string_reversal_button = tk.Button(t, text="Reverse!", command = stringReversal)
string_reversal_button.pack()

file_list = []
updatedFiles = []
updatedPaths = []


save_text_label = tk.Label(text = "Save Text")
save_text_label.pack()
t.mainloop()

