import os
import sys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Ventana con icono")
if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "icon.ico")
else:
    root.wm_iconbitmap(bitmap = "@icon.xbm")

root.mainloop()
