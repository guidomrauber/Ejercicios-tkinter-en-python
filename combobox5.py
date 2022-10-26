from tkinter import messagebox, ttk
import tkinter as tk
def selection_changed(event):
    selection = combo.get()
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=50)
main_window.mainloop()