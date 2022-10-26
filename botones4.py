import tkinter as tk
class BotonPeligro(tk.Button):
    def __init__(self, *args, **kwargs):
        # Procurar no reemplazar los argumentos provistos.
        if "foreground" not in kwargs:
            kwargs["foreground"] = "#ff0000"
        if "activeforeground" not in kwargs:
            kwargs["activeforeground"] = "#FFA500"
        super().__init__(*args, **kwargs)
ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("Apariencia de controles clásicos")
boton = BotonPeligro(text="¡Hola, mundo!")
boton.place(x=40, y=50)
ventana.mainloop()