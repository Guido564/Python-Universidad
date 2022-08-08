from textwrap import wrap
from time import sleep
import tkinter as tk
from tkinter import Label, ttk, messagebox, scrolledtext
from turtle import width
from time import sleep

ventana = tk.Tk()
ventana.geometry('800x800')
ventana.title('Hola soy una ventana ja')

imagen = tk.PhotoImage(file="57. Componentes en Tkinter\Tarea 1\Cheryl.png")

def componentes_tabulador1(tabulador):
    #Etiqueta y componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Su nombre de usuario:')
    etiqueta1.grid(row=0, column=0, padx=5, pady=5)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)
    etiqueta2 = ttk.Label(tabulador, text='Su pass si se atreve:')
    etiqueta2.grid(row=1, column=0, padx=5, pady=5)
    entrada2 = ttk.Entry(tabulador, width=30, show='*')
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

    boton1 = ttk.Button(tabulador, text='Lo quiere enviar?', command=enviar)
    boton1.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
    
def componentes_tabulador2(tabulador):
    contenido = '''«Ay», dijo el ratón, «el mundo se está haciendo más chiquito cada día. Al principio era tan grande que yo tenía miedo, corría y corría, y me alegraba cuando al fin veía paredes a lo lejos a diestra y siniestra, pero estas largas paredes se han achicado tanto que ya estoy en la última cámara, y ahí en la esquina está la trampa a la cual yo debo caer». «Sólamente tienes que cambiar tu dirección», dijo el gato, y se lo comió. 
                                            -Fran Kafka'''

    scroll = scrolledtext.ScrolledText(tabulador, width=100, height=462, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    scroll.grid(row=0, column=0)
    
def componentes_tabulador3(tabulador):
    etiqueta1 = ttk.Label(tabulador, text='Del 1 al 10 que tanto le gusto el cuento anterior?')
    etiqueta1.grid(row=0, column=0, padx=5, pady=5)
    
    datos = [x + 1 for x in range(11)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=1, column=0)
    
    def enviar():
        if len(combobox.get()) == 0:
            messagebox.showerror('Nanana!', 'Elegi una opcion')
        else:    
            messagebox.showinfo('Datos?', f'Opcion seleccionada: {combobox.get()}')
    
    boton1 = ttk.Button(tabulador, text='Lo quiere enviar?', command=enviar)
    boton1.grid(row=2, column=0, padx=5, pady=5)


def componentes_tabulador4(tabulador):
    def info():
        messagebox.showinfo('Esto es lo que hay', 'https://silenthill.fandom.com/es/wiki/Cheryl_Mason')
    
    label = Label(image=imagen)
    label.pack()
    boton_imagen = ttk.Button(tabulador, image=imagen, command=info)
    boton_imagen.grid(row=0, column=0)
    
def componentes_tabulador5(tabulador):
    barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=750)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    
    def ejecutar():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            sleep(0.05)
            barra_progreso['value'] = valor
            barra_progreso.update()
        barra_progreso['value'] = 0
    
    def ejecutar_ciclo():
        barra_progreso.start()
        
    def detener():
        barra_progreso.stop()
    
    def detener_segundos():
        esperar_ms = 1000
        ventana.after(esperar_ms, barra_progreso.stop)
    
    boton_inicio = ttk.Button(tabulador,
                              text='Ejecutar el progreso', command=ejecutar)
    boton_inicio.grid(row=1, column=0)
    boton_ciclo = ttk.Button(tabulador,
                              text='Ejecutar ciclo', command=ejecutar_ciclo)
    boton_ciclo.grid(row=1, column=1)
    boton_detener = ttk.Button(tabulador,
                              text='Detener ejecucion', command=detener)
    boton_detener.grid(row=1, column=2)
    boton_detener_segundos = ttk.Button(tabulador,
                              text='Detener ejecucion a los segundos', command=detener_segundos)
    boton_detener_segundos.grid(row=1, column=3)
    
def crear_tabs():
    #Tab control
    control_tabulador = ttk.Notebook(ventana)
    #Frame para organizar elementos dentro del tab
    tabulador1 = ttk.Frame(control_tabulador)
    tabulador2 = ttk.LabelFrame(control_tabulador, text='Una pequenia fabula')
    tabulador3 = ttk.Frame(control_tabulador)
    tabulador4 = ttk.Frame(control_tabulador)
    tabulador5 = ttk.Frame(control_tabulador)
    #Control de tabuladores
    control_tabulador.add(tabulador1, text='El primero de muchos')
    control_tabulador.add(tabulador2, text='El segundo hermano')
    control_tabulador.add(tabulador3, text='Estoy para datos (3)')
    control_tabulador.add(tabulador4, text='Cheryl')
    control_tabulador.add(tabulador5, text='Barras para progresar')
    #Se ve el tabulador lindo
    control_tabulador.pack(fill='both')
    #Creacion componentes tabulador1
    componentes_tabulador1(tabulador1)
    #Creacion componentes tabulador2
    componentes_tabulador2(tabulador2)
    #Creacion componentes tabulador3
    componentes_tabulador3(tabulador3)
    #Creacion componentes tabulador4
    componentes_tabulador4(tabulador4)
    #Creacion componentes tabulador5
    componentes_tabulador5(tabulador5)

crear_tabs()

ventana.mainloop()