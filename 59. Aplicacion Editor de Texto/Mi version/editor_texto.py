from ctypes.wintypes import WORD
import tkinter as tk
from tkinter import INSERT, ttk, Menu, Text

ventana = tk.Tk()
ventana.geometry('900x600')
ventana.title('Hola soy un editor de texto')

def editor_texto():
    texto = Text(ventana, width=112, height=600, wrap=tk.WORD)
    texto.grid(row=0, column=0)
    
def crear_menu():
    menuPrincipal = Menu(ventana)
    subMenuArchivo = Menu(menuPrincipal, tearoff=0)
    subMenuArchivo.add_command(label='Abrir')
    subMenuArchivo.add_command(label='Guardar')
    subMenuArchivo.add_command(label='Guardar como...')
    subMenuArchivo.add_separator()
    subMenuArchivo.add_command(label='Salir')
    menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
    
    ventana.config(menu=menuPrincipal)

crear_menu()
editor_texto()
ventana.mainloop()