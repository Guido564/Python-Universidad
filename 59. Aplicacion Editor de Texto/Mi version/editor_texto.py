from ctypes.wintypes import WORD
import tkinter as tk
from tkinter import INSERT, ttk, Menu, Text

ventana = tk.Tk()
ventana.geometry('900x600')
ventana.title('Hola soy un editor de texto')

texto = Text(ventana, width=112, height=600, wrap=tk.WORD)
texto.grid(row=0, column=0)

def editar():
    esto_se_guarda = texto.get('1.0','end-1c')
    with open('guardado_default.txt', 'w') as g:
        g.write(esto_se_guarda)

    
def crear_menu():
    menuPrincipal = Menu(ventana)
    subMenuArchivo = Menu(menuPrincipal, tearoff=0)
    subMenuArchivo.add_command(label='Abrir')
    subMenuArchivo.add_command(label='Guardar', command=editar)
    subMenuArchivo.add_command(label='Guardar como...')
    subMenuArchivo.add_separator()
    subMenuArchivo.add_command(label='Salir')
    menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
    
    ventana.config(menu=menuPrincipal)

crear_menu()
ventana.mainloop()