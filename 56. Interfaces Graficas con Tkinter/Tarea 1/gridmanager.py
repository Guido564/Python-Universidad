import tkinter as tk
from tkinter import mainloop, ttk

ventana = tk.Tk()
ventana.geometry('600x600')
ventana.title('Progamita humilde')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text='Hola soy B1')
boton1.grid(row=0, column=0, sticky='NSWE')

boton2 = ttk.Button(ventana, text='Hola soy B2')
boton2.grid(row=1, column=0, sticky='NSWE')

mainloop()