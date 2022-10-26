import tkinter as tk
from tkinter import ttk
class VentanaSecundaria(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=300, height=200)
        self.title("Ventana secundaria")
        self.boton_cerrar = ttk.Button(
            self,
            text="Cerrar ventana",
            command=self.destroy
        )
        self.boton_cerrar.place(x=75, y=75)
        self.focus()
        self.grab_set()
class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Ventana principal")
        self.boton_abrir = ttk.Button(
            self,
            text="Abrir ventana secundaria",
            command=self.abrir_ventana_secundaria
        )
        self.boton_abrir.place(x=100, y=100)
    def abrir_ventana_secundaria(self):
        self.ventana_secundaria = VentanaSecundaria()
ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()