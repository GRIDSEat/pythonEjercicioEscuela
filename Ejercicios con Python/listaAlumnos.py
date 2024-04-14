class Alumnos:
    def __init__(self):
        self.nombre = []
        self.nota = []

    def menu(self):
        opcion = 0
        while opcion != 4:
            print('1: Carga de alumnos')    
            print('2 Listar alumnos')
            print('3 Mostrar alumnos con notas mayores o iguales a 7')
            print('4 Finalizar tareas')
            opcion = int(input('Ingrese número'))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.notas_altas()

    def cargar(self):
        for x in range (5):
            nom = input('Ingrese el nombre del alumno ')
            self.nombre.append(nom)
            nota = int(input('Ingrese nota'))
            self.nota.append(nota) 

    def listar(self):
        print ('La lista de alumnos cargada es: ')
        for x in range(5):
            print(self.nombre[x],self.nota[x])
        print('--------------------------------------')

    def notas_altas(self):
        print('Los alumnos que tienen notas iguales o superiores a sieta son:')
        for x in range(5):
            if self.nota[x] >= 7:
                print(self.nombre[x],self.nota[x])


alumnos = Alumnos()
alumnos.menu()