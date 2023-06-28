import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, simpledialog

t = Tk()

t.geometry("700x700")
t.title("File Renamer")

file_list = []


numberOfFiles = simpledialog.askinteger("File Renamer", "How many files?")

for i in range(numberOfFiles):
    file_path = filedialog.askopenfilename()
    file_list.append(file_path)

fileRename = simpledialog.askstring("File Rename", "Rename as?")

for i in range(numberOfFiles):
    file_extension = os.path.splitext(file_path)[1]
    os.rename(file_list[i], f"{fileRename}_{i}{file_extension}")

t.mainloop()

