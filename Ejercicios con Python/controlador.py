from tkinter import *
from vista import *
class principal ():
    def __init__(self,):
        self.ventana = Tk()
    def lanzaApp(self):
        marco(self.ventana)
        self.ventana.mainloop()


if __name__  == '__main__':
    
    comienzo = principal()
    comienzo.lanzaApp()
    