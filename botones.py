from tkinter import ttk
import tkinter as tk
ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("Estilos en Tk")
boton = ttk.Button(text="¡Hola, mundo!")
boton.place(x=40, y=50)
ventana.mainloop()