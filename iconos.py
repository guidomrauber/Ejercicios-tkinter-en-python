import tkinter as tk
ventana = tk.Tk()
ventana.title("Ventana con ícono")
ventana.geometry("300x200")
# Cargar el archivo de imagen desde el disco.
icono = tk.PhotoImage(file="icon-16.png")
# Establecerlo como ícono de la ventana.
ventana.iconphoto(True, icono)
ventana.mainloop()