import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Hola soy una ventana ja')

def crear_tabs():
    #Tab control
    control_tabulador = ttk.Notebook(ventana)
    #Frame para organizar elementos dentro del tab
    tabulalodor1= ttk.Frame(control_tabulador)
    #Tabulador al control de tabuladores
    control_tabulador.add(tabulalodor1, text='El primero de muchos')
    #Se ve el tabulador lindo
    control_tabulador.pack(fill='both')
    
    #Etiqueta y componente de entrada
    etiqueta1 = ttk.Label(tabulalodor1, text='Su nombre de usuario:')
    etiqueta1.grid(row=0, column=0, padx=5, pady=5)
    entrada1 = ttk.Entry(tabulalodor1, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)
    etiqueta2 = ttk.Label(tabulalodor1, text='Su pass si se atreve:')
    etiqueta2.grid(row=1, column=0, padx=5, pady=5)
    entrada2 = ttk.Entry(tabulalodor1, width=30, show='*')
    entrada2.grid(row=1, column=1, padx=5, pady=5)
    #Boton
    def enviar():
        user = entrada1.get()
        password = entrada2.get()
        
        if len(user + password) == 0:
            messagebox.showerror('Datos!', 'Ponele onda man')
        elif len(password) == 0:
            messagebox.showinfo('Datos?', f'Senior usuario: {user}, meteme una pass pls')
        elif len(user) == 0:
            messagebox.showinfo('Tomada de pelo', f'Contrasenia sin user? Senior esto es la NASA')
        else:
            messagebox.showinfo('Datos', f'Su nombre de usuario es: {user}\nSu pass es: {password}')

    
    boton1 = ttk.Button(tabulalodor1, text='Lo quiere enviar?', command=enviar)
    boton1.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
    

crear_tabs()

ventana.mainloop()