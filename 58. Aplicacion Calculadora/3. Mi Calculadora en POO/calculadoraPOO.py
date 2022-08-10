import tkinter as tk
from tkinter import INSERT, ttk, messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.title('Soy una calculadora en objetos O:')
        self.resizable(0,0)
        self.iconbitmap('58. Aplicacion Calculadora\Calculator.ico')
        
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=3)
        self.rowconfigure(3, weight=3)
        self.rowconfigure(4, weight=3)
        self.rowconfigure(5, weight=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        
        self.ingreso_operaciones = ttk.Entry(self, width=20, justify='right')
        self.ingreso_operaciones.grid(row=0, column=0, columnspan=4, sticky='NSWE')
        
        self._crear_componentes()
    
    def _crear_componentes(self):
        boton_c = ttk.Button(self, text='C', command=self._reiniciar)
        boton_c.grid(row=1, column=0, columnspan=3, sticky='NSWE')
        boton_barra = ttk.Button(self, text='/', command= lambda: self._ingreso_dato('/'))
        boton_barra.grid(row=1, column=3, sticky='NSWE')
        
        boton_7 = ttk.Button(self, text='7', command=lambda: self._ingreso_dato('7'))
        boton_7.grid(row=2, column=0, sticky='NSWE')
        boton_8 = ttk.Button(self, text='8', command=lambda: self._ingreso_dato('8'))
        boton_8.grid(row=2, column=1, sticky='NSWE')
        boton_9 = ttk.Button(self, text='9', command=lambda: self._ingreso_dato('9'))
        boton_9.grid(row=2, column=2, sticky='NSWE')
        boton_mul = ttk.Button(self, text='*', command=lambda: self._ingreso_dato('*'))
        boton_mul.grid(row=2, column=3, sticky='NSWE')
        
        boton_4 = ttk.Button(self, text='4', command=lambda: self._ingreso_dato('4'))
        boton_4.grid(row=3, column=0, sticky='NSWE')
        boton_5 = ttk.Button(self, text='5', command=lambda: self._ingreso_dato('5'))
        boton_5.grid(row=3, column=1, sticky='NSWE')
        boton_6 = ttk.Button(self, text='6', command=lambda: self._ingreso_dato('6'))
        boton_6.grid(row=3, column=2, sticky='NSWE')
        boton_resta = ttk.Button(self, text='-', command=lambda: self._ingreso_dato('-'))
        boton_resta.grid(row=3, column=3, sticky='NSWE')
        
        boton_1 = ttk.Button(self, text='1', command=lambda: self._ingreso_dato('1'))
        boton_1.grid(row=4, column=0, sticky='NSWE')
        boton_2 = ttk.Button(self, text='2', command=lambda: self._ingreso_dato('2'))
        boton_2.grid(row=4, column=1, sticky='NSWE')
        boton_3 = ttk.Button(self, text='3', command=lambda: self._ingreso_dato('3'))
        boton_3.grid(row=4, column=2, sticky='NSWE')
        boton_suma = ttk.Button(self, text='+', style="Custom.TButton", command=lambda: self._ingreso_dato('+'))
        boton_suma.grid(row=4, column=3, sticky='NSWE')
        
        boton_0 = ttk.Button(self, text='0', command=lambda: self._ingreso_dato('0'))
        boton_0.grid(row=5, column=0, columnspan=2, sticky='NSWE')
        boton_float = ttk.Button(self, text='.', command=lambda: self._ingreso_dato('.'))
        boton_float.grid(row=5, column=2, sticky='NSWE')
        boton_igual = ttk.Button(self, text='=', command=self._evaluar_operacion)
        boton_igual.grid(row=5, column=3, sticky='NSWE')
        
    def _ingreso_dato(self, dato):
            self.ingreso_operaciones.insert(INSERT, dato)
            
    def _reiniciar(self):
        self.ingreso_operaciones.delete(0, 'end')
        
    def _evaluar_operacion(self):
        try:
            if self.ingreso_operaciones.get():
                operacion = self.ingreso_operaciones.get()
                resultado = eval(operacion)
                self.ingreso_operaciones.delete(0, 'end')
                self.ingreso_operaciones.insert(INSERT, resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Deje nene que se rompe el programita: {e}')
            self.ingreso_operaciones.delete(0, 'end')

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()