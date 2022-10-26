import tkinter as tk
ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("Apariencia de controles clásicos")
boton = tk.Button(text="¡Hola, mundo!", foreground="#ff0000",
                  activeforeground="#FFA500")
boton.place(x=40, y=50)
ventana.mainloop()