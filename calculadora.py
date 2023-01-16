import tkinter as tk

class Interfaz:
    def __init__ (self, ventana):
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.ventana.config(bg='darkgrey')
        self.pantalla = tk.Text(ventana, state='disabled', width=40, height=3, background = 'lightgreen', foreground= 'white',font=('helvetia', 14))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        self.operacion=''
        self.resultado=''
        
        boton1= self.CrearBoton(7)
        boton2= self.CrearBoton(8)
        boton3= self.CrearBoton(9)
        boton4= self.CrearBoton(u'\u232B', escribir=False) #flechita para atras
        boton5= self.CrearBoton(4)
        boton6= self.CrearBoton(5)
        boton7= self.CrearBoton(6)
        boton8= self.CrearBoton(u'\u00f7') #dividido
        boton9= self.CrearBoton(1)
        boton10= self.CrearBoton(2)
        boton11= self.CrearBoton(3)
        boton12= self.CrearBoton('-')
        boton13= self.CrearBoton('.')
        boton14= self.CrearBoton(0)
        boton15= self.CrearBoton('+')
        boton16= self.CrearBoton('*')
        boton17= self.CrearBoton('=', escribir=False, ancho=20, alto=2)
        
        botones=[boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador=contador+1
        botones[16].grid(row=5,column=0, columnspan=4)
    
    def CrearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return tk.Button (self.ventana, text=valor, width=ancho, height=alto, font=('helvetica, 15'), command= lambda: self.click(valor, escribir))
    
    def click(self, text, escribir):
        if escribir==False:
            if text=='=' and self.operacion!='':
                self.operacion=tk.re.sub(u"\u00F7", "/", self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=''
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            elif text==u'\u232B':
                self.operacion=''
                self.limpiarPantalla()
        else:
            self.operacion=self.operacion+ str(text)
            self.mostrarEnPantalla(text)
        return
    
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state='normal')
        self.pantalla.insert(tk.END, valor)
        self.pantalla.configure(state='disabled')
        return

    def limpiarPantalla(self):
        self.pantalla.configure(state='normal')
        self.pantalla.delete(1.0, tk.END)
        self.pantalla.configure(state='disabled')
        return

ventana_principal = tk.Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
