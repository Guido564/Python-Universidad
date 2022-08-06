from distutils.log import Log
import sys
import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x100')
        self.title('Login')
        self.resizable(0, 0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)
        
        self._crearComponentes()
    
    def _crearComponentes(self):
        usuarioEt = tk.Label(self, text='Usuario:')
        usuarioEt.grid(row=1, column=0, sticky='E')
        self.usuario = ttk.Entry(self, width=30)
        self.usuario.grid(row=1, column=1, sticky='E')

        passEt = tk.Label(self, text='Password:')
        passEt.grid(row=2, column=0, sticky='E')
        self.password = ttk.Entry(self, width=30, show='*')
        self.password.grid(row=2, column=1, sticky='E')
        
        self.enviar1 = ttk.Button(self, text='Enviar', command=self._enviar)
        self.enviar1.grid(row=3, column=1)

    def _enviar(self):
        usuarioData = self.usuario.get()
        pasData = self.password.get()
        
        messagebox.showinfo('Datos del usuario', f'Usuario: {usuarioData}\nContrasenia: {pasData}')
        
        self.enviar1.config(text='Enviado!')

loginVentana = Login()
loginVentana.mainloop()