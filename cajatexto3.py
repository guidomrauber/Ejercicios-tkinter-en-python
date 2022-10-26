import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
style = ttk.Style()
style.configure(
    "MyEntry.TEntry",
    # Fondo rojo.
    fieldbackground="#ff0000",
    # Color de texto azul.
    foreground="#0000ff"
)
entry = ttk.Entry(style="MyEntry.TEntry")
entry.place(x=50, y=50)
root.mainloop()