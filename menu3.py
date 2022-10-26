import tkinter as tk
def archivo_nuevo_presionado(event=None):
    print("¡Has presionado para crear un nuevo archivo!")
ventana = tk.Tk()
ventana.title("Barra de menús en Tk")
ventana.config(width=400, height=300)
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
img_menu_nuevo = tk.PhotoImage(file="nuevo_archivo.png")
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=archivo_nuevo_presionado,
    image=img_menu_nuevo,
    # Indicar que la imagen debe aparecer a la izquierda del texto.
    compound=tk.LEFT
)
ventana.bind_all("<Control-n>", archivo_nuevo_presionado)
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
ventana.config(menu=barra_menus)
ventana.mainloop()