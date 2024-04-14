from tkinter import *
def marco(ventana):
    ventana.geometry('500x200')
    ventana.title('Principal')
    etiquetaEntrada = Label(ventana,text='Ingrese Número')
    etiquetaEntrada.grid(row=0,column=0,padx=10,pady=10)
    entrada = Entry(ventana,)
    entrada.grid(row=0,column=1,padx=10,pady=10)
    salida = Entry(ventana)
    salida.grid(row=1,column=1,pady=10,padx=10)



    def ingresoNumero():
        salida.delete(0,END)
        numero = int(entrada.get())
        salida.insert(0,numero)
        
    boton = Button(ventana,text= 'Ingrese número', command=ingresoNumero)
    boton.grid(row=2,column=1)

    ventana.mainloop()