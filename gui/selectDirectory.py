import tkinter as tk
from tkinter import filedialog

def getDirectory():
    getDir = tk.Tk()
    getDir.withdraw()
    file_path = filedialog.askdirectory(title="Selecciona la carpeta dee búsqueda")
    return file_path

#print(getDirectory())
