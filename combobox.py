
from tkinter import ttk
import tkinter as tk
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox()
combo.place(x=50, y=50)
main_window.mainloop()