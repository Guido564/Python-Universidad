import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x600')
ventana.title('Manejo de Componentes')

def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

def crearMenu():
    menuPrincipal = Menu(ventana)
    subMenuArchivo = Menu(menuPrincipal, tearoff=0)
    subMenuArchivo.add_command(label='Nuevo')
    subMenuArchivo.add_command(label='Abrir')
    subMenuArchivo.add_command(label='Guardar')
    subMenuArchivo.add_separator()
    subMenuArchivo.add_command(label='Salir', command=salir)
    menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
    
    subMenuAyuda = Menu(menuPrincipal, tearoff=0)
    subMenuAyuda.add_command(label='Documentacion')
    subMenuAyuda.add_command(label='Ayuda')
    subMenuAyuda.add_command(label='Acerca de')
    menuPrincipal.add_cascade(menu=subMenuAyuda, label='Informacion')
    
    ventana.config(menu=menuPrincipal)
    

crearMenu()
ventana.mainloop()