import tkinter as tk
from tkinter import INSERT, ttk, messagebox

ventana = tk.Tk()
ventana.geometry('400x450')
ventana.title('Hola soy una calculadora')
ventana.resizable(0,0)
ventana.iconbitmap('58. Aplicacion Calculadora\Calculator.ico')

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=3)
ventana.rowconfigure(2, weight=3)
ventana.rowconfigure(3, weight=3)
ventana.rowconfigure(4, weight=3)
ventana.rowconfigure(5, weight=3)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

ingreso_operaciones = ttk.Entry(ventana, width=20, justify='right')
ingreso_operaciones.grid(row=0, column=0, columnspan=4, sticky='NSWE')

def agregar0():
    ingreso_operaciones.insert(INSERT, '0')
        
def agregar1():
    ingreso_operaciones.insert(INSERT, '1')

def agregar2():
    ingreso_operaciones.insert(INSERT, '2')
        
def agregar3():
    ingreso_operaciones.insert(INSERT, '3')

def agregar4():
    ingreso_operaciones.insert(INSERT, '4')
        
def agregar5():
    ingreso_operaciones.insert(INSERT, '5')
    
def agregar6():
    ingreso_operaciones.insert(INSERT, '6')
        
def agregar7():
    ingreso_operaciones.insert(INSERT, '7')

def agregar8():
    ingreso_operaciones.insert(INSERT, '8')
        
def agregar9():
    ingreso_operaciones.insert(INSERT, '9')
    
def agregar_float():
    ingreso_operaciones.insert(INSERT, '.')
    
def agregar_multiplicacion():
    ingreso_operaciones.insert(INSERT, '*')

def agregar_division():
    ingreso_operaciones.insert(INSERT, '/')
    
def agregar_resta():
    ingreso_operaciones.insert(INSERT, '-')

def agregar_suma():
    ingreso_operaciones.insert(INSERT, '+')
    
def reiniciar():
    ingreso_operaciones.delete(0, 'end')
    
def evaluar_operacion():
    try:
        if ingreso_operaciones.get():
            operacion = ingreso_operaciones.get()
            resultado = eval(operacion)
            ingreso_operaciones.delete(0, 'end')
            ingreso_operaciones.insert(INSERT, resultado)
    except Exception as e:
        messagebox.showerror('Error', f'Deje nene que se rompe el programita: {e}')
        ingreso_operaciones.delete(0, 'end')
    
def crear_componentes():
    
    boton_c = ttk.Button(ventana, text='C', command=reiniciar, style="Custom.TButton")
    boton_c.grid(row=1, column=0, columnspan=3, sticky='NSWE')
    boton_barra = ttk.Button(ventana, text='/', command=agregar_division, style="Custom.TButton")
    boton_barra.grid(row=1, column=3, sticky='NSWE')
    
    boton_7 = ttk.Button(ventana, text='7', command=agregar7)
    boton_7.grid(row=2, column=0, sticky='NSWE')
    boton_8 = ttk.Button(ventana, text='8', command=agregar8)
    boton_8.grid(row=2, column=1, sticky='NSWE')
    boton_9 = ttk.Button(ventana, text='9', command=agregar9)
    boton_9.grid(row=2, column=2, sticky='NSWE')
    boton_mul = ttk.Button(ventana, text='*', command=agregar_multiplicacion, style="Custom.TButton")
    boton_mul.grid(row=2, column=3, sticky='NSWE')
    
    boton_4 = ttk.Button(ventana, text='4', command=agregar4)
    boton_4.grid(row=3, column=0, sticky='NSWE')
    boton_5 = ttk.Button(ventana, text='5', command=agregar5)
    boton_5.grid(row=3, column=1, sticky='NSWE')
    boton_6 = ttk.Button(ventana, text='6', command=agregar6)
    boton_6.grid(row=3, column=2, sticky='NSWE')
    boton_resta = ttk.Button(ventana, text='-', command=agregar_resta, style="Custom.TButton")
    boton_resta.grid(row=3, column=3, sticky='NSWE')
    
    boton_1 = ttk.Button(ventana, text='1', command=agregar1)
    boton_1.grid(row=4, column=0, sticky='NSWE')
    boton_2 = ttk.Button(ventana, text='2', command=agregar2)
    boton_2.grid(row=4, column=1, sticky='NSWE')
    boton_3 = ttk.Button(ventana, text='3', command=agregar3)
    boton_3.grid(row=4, column=2, sticky='NSWE')
    boton_suma = ttk.Button(ventana, text='+', command=agregar_suma, style="Custom.TButton")
    boton_suma.grid(row=4, column=3, sticky='NSWE')
    
    boton_0 = ttk.Button(ventana, text='0', command=agregar0)
    boton_0.grid(row=5, column=0, columnspan=2, sticky='NSWE')
    boton_float = ttk.Button(ventana, text='.', command=agregar_float)
    boton_float.grid(row=5, column=2, sticky='NSWE')
    boton_igual = ttk.Button(ventana, text='=', command=evaluar_operacion, style="Custom.TButton")
    boton_igual.grid(row=5, column=3, sticky='NSWE')


crear_componentes()

ventana.mainloop()