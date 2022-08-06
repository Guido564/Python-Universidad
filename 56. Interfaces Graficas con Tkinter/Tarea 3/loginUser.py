import sys
import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('250x100')
ventana.title('Login')

ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(2, weight=1)
ventana.columnconfigure(2, weight=1)


usuarioEt = tk.Label(ventana, text='Usuario:')
usuarioEt.grid(row=0, column=0, sticky='E')
usuario = ttk.Entry(ventana, width=30)
usuario.grid(row=0, column=1, sticky='E')

passEt = tk.Label(ventana, text='Password:')
passEt.grid(row=1, column=0, sticky='E')
password = ttk.Entry(ventana, width=30, show='*')
password.grid(row=1, column=1, sticky='E')

def enviar():
    usuarioData = usuario.get()
    pasData = password.get()
    
    messagebox.showinfo('Datos del usuario', f'Usuario: {usuarioData}\nContrasenia: {pasData}')
    
    enviar1.config(text='Enviado!')

enviar1 = ttk.Button(ventana, text='Enviar', command=enviar)
enviar1.grid(row=2, column=1)


ventana.mainloop()