
class Alumno:
    def __init__(self):
        self.nombre = []
        self.nota = []
        
    def menu(self):
        opcion=0
        while opcion != 4:
            print('1: Carga ')
            print('2 lista ')
            print('3 muestra ')
            print('4 finaliza ')
            opcion = int(input('ingresa opcion '))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.lista()
            elif opcion == 3:
                self.notas_altas()
                    
    def cargar(self):
        for x in range (5):
            nom = input('Ingrese el nombre del alumno ')
            self.nombre.append(nom)
            nota_numerica = int(input('Ingrese nota '))
            self.nota.append(nota_numerica)
            
    def lista(self):
        try:
            print('La lista de alumno con igual o mayor que 7: ')
            for i in range (5):
                if self.nota[i]>=7:
                    print(self.nombre[i], self.nota[i]) 
        except IndexError: 
            print('la lista no esta llena')
              
alumno = Alumno()
alumno.menu()