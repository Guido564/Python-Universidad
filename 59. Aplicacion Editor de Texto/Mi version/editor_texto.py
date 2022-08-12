import tkinter as tk
from tkinter import Text, Menu, ttk
from tkinter import filedialog

def abrir():
    if not texto.edit_modified(): 
        try:
            path = filedialog.askopenfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
                       
            ventana.title('Notepad - ' + path)
            
            with open(path, 'r') as f:
                content = f.read()
                texto.delete('1.0', tk.END)
                texto.insert('1.0', content)
                                
                texto.edit_modified(0)
             
        except:
            pass
    
    else:
        guardar_como()
        
        texto.edit_modified(0)
        abrir()
    
def guardar():
    try:
        
        path = ventana.title().split('-')[1][1:]
    
    except:
        path = ''
    
    if path != '':
        
        with open(path, 'w') as f:
            content = texto.get('1.0', tk.END)
            f.write(content)
      
    else:
        guardar_como()
    
    texto.edit_modified(0)

def guardar_como():
    try:
        path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        ventana.title('Notepad - ' + path)
    
    except:
        return
    
    with open(path, 'w') as f:
        f.write(texto.get('1.0', tk.END))


ventana = tk.Tk()
ventana.geometry('900x600')
ventana.title('Hola soy un editor de texto')

texto = Text(ventana)
texto.pack(expand = tk.YES, fill = tk.BOTH, side = tk.LEFT)

scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=texto.yview)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
texto['yscrollcommand'] = scrollbar.set

def crear_menu():
    menuPrincipal = Menu(ventana)
    subMenuArchivo = Menu(menuPrincipal, tearoff=0)
    subMenuArchivo.add_command(label='Abrir', command=abrir)
    subMenuArchivo.add_command(label='Guardar', command=guardar)
    subMenuArchivo.add_command(label='Guardar como...', command=guardar_como)
    subMenuArchivo.add_separator()
    subMenuArchivo.add_command(label='Salir', command=ventana.quit)
    menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
    
    ventana.config(menu=menuPrincipal)

crear_menu()
ventana.mainloop()