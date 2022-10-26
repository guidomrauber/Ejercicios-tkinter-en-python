import tkinter as tk
ventana = tk.Tk()
ventana.title("Ventana con ícono")
ventana.geometry("300x200")
icono_chico = tk.PhotoImage(file="icon-16.png")
icono_grande = tk.PhotoImage(file="icon-32.png")
ventana.iconphoto(True, icono_grande)
ventana.mainloop()