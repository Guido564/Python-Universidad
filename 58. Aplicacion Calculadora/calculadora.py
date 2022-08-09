import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('553x645')
ventana.title('Hola soy una calculadora')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

def crear_componentes():
    ingreso_operaciones = ttk.Entry(ventana, width=20, justify='right')
    ingreso_operaciones.grid(row=0, column=0, columnspan=4, sticky='NSWE')
    
    boton_c = ttk.Button(ventana, text='C')
    boton_c.grid(row=1, column=0, columnspan=3, sticky='NSWE')
    boton_barra = ttk.Button(ventana, text='/')
    boton_barra.grid(row=1, column=3, sticky='NSWE')
    
    boton_7 = ttk.Button(ventana, text='7')
    boton_7.grid(row=2, column=0, sticky='NSWE')
    boton_8 = ttk.Button(ventana, text='8')
    boton_8.grid(row=2, column=1, sticky='NSWE')
    boton_9 = ttk.Button(ventana, text='9')
    boton_9.grid(row=2, column=2, sticky='NSWE')
    boton_mul = ttk.Button(ventana, text='*')
    boton_mul.grid(row=2, column=3, sticky='NSWE')
    
    boton_4 = ttk.Button(ventana, text='4')
    boton_4.grid(row=3, column=0, sticky='NSWE')
    boton_5 = ttk.Button(ventana, text='5')
    boton_5.grid(row=3, column=1, sticky='NSWE')
    boton_6 = ttk.Button(ventana, text='6')
    boton_6.grid(row=3, column=2, sticky='NSWE')
    boton_resta = ttk.Button(ventana, text='-')
    boton_resta.grid(row=3, column=3, sticky='NSWE')
    
    boton_1 = ttk.Button(ventana, text='1')
    boton_1.grid(row=4, column=0, sticky='NSWE')
    boton_2 = ttk.Button(ventana, text='2')
    boton_2.grid(row=4, column=1, sticky='NSWE')
    boton_3 = ttk.Button(ventana, text='3')
    boton_3.grid(row=4, column=2, sticky='NSWE')
    boton_suma = ttk.Button(ventana, text='+')
    boton_suma.grid(row=4, column=3, sticky='NSWE')
    
    boton_0 = ttk.Button(ventana, text='0')
    boton_0.grid(row=5, column=0, columnspan=2, sticky='NSWE')
    boton_float = ttk.Button(ventana, text='.')
    boton_float.grid(row=5, column=2, sticky='NSWE')
    boton_igual = ttk.Button(ventana, text='=')
    boton_igual.grid(row=5, column=3, sticky='NSWE')

crear_componentes()





ventana.mainloop()