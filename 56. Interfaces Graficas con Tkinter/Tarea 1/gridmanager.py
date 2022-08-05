import tkinter as tk
from tkinter import Button, mainloop, ttk

ventana = tk.Tk()
ventana.geometry('600x600')
ventana.title('Progamita humilde')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

def intenciones():
    boton1.config(text='Intenciones desconocidas')

boton1 = ttk.Button(ventana, text='Hola soy B1', command=intenciones)
boton1.grid(row=0, column=0, sticky='NSWE')

boton2 = ttk.Button(ventana, text='Hola soy B2')
boton2.grid(row=1, column=0, sticky='NSWE')

boton3 = ttk.Button(ventana, text='Hola soy B3')
boton3.grid(row=0, column=1, sticky='NSWE')

boton4 = ttk.Button(ventana, text='Hola soy B4')
boton4.grid(row=1, column=1, sticky='NSWE')

mainloop()