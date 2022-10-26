import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
entry = ttk.Entry()
entry.place(x=50, y=50)
# Esta segunda caja de texto no puede recibir el foco
# vía la tecla Tab.
entry2 = ttk.Entry(takefocus=False)
entry2.place(x=50, y=150)
root.mainloop()