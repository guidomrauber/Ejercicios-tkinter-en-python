import tkinter as tk
root = tk.Tk()
root.config(width=300, height=200)
# Nótese tk.Entry en lugar de ttk.Entry.
entry = tk.Entry(
    # Color del fondo.
    background="#ff0000",
    # Color del texto.
    foreground="#0000ff",
)
entry.place(x=50, y=50)
root.mainloop()