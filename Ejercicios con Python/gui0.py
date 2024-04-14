from tkinter import *
def intro():
    ingreso =str( input ("Introducir título: ")  )  
    geometria =str( input("Introducir geometría: "))
    return (ingreso, geometria)


class dibujo:
    
    def __init__(self,titulo,geometria):
        self.ventana = Tk()
        self.titulo = titulo
        self.geometria =geometria
        self.constante = 4
        
    
    def creacion(self):
        self.ventana.geometry(self.geometria)
        self.ventana.title(self.titulo)
        lista = [25,3]
        for i in range(self.constante):
            lista.append(i)
        print (lista)
        variable1 = StringVar()
        variable2 = StringVar()
        variable3 = StringVar()
        def suma():
            try:
                elemento1 = float(variable1.get())
                elemento2 = float(variable2.get())
                salida = (elemento1  + elemento2)/2
                print(salida)
                variable3.set(salida)
            except:
                variable3.set("Incorrecto")
        entrada1 = Entry(self.ventana,textvariable=variable1)
        entrada2 = Entry(self.ventana,textvariable=variable2)
        salida = Entry(self.ventana,textvariable=variable3)
        salida.grid(row=0,column=4)
        entrada1.grid(row=0,column=0,padx=10,pady=10)
        entrada2.grid(row=1,column=0,padx=10,pady=10)
        boton = Button(self.ventana,text="Suma",command=suma)
        boton.grid(row=0,column=2)
        self.ventana.mainloop()
    def modificacion(self,numero):
            pass

    
    


tupla = intro()
titulo = tupla[0]
geometria = tupla[1]
dibu = dibujo(titulo, geometria)
dibu.creacion()
