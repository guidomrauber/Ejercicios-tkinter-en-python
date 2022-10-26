import tkinter as tk
def archivo_nuevo_presionado(event=None):
    print("¡Has presionado para crear un nuevo archivo!")
def menu_iniciar_con_sistema_presionado():
    if iniciar_con_sistema.get():
        print("Opción establecida (iniciar con el sistema).")
    else:
        print("Opción deshabilitada (no iniciar con el sistema).")
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
    compound=tk.LEFT
)
ventana.bind_all("<Control-n>", archivo_nuevo_presionado)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)
menu_opciones = tk.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = tk.BooleanVar()
menu_opciones.add_checkbutton(
    label="Iniciar con sistema",
    command=menu_iniciar_con_sistema_presionado,
    variable=iniciar_con_sistema
)
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Opciones")
ventana.config(menu=barra_menus)
ventana.mainloop()