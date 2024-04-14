class agenda:
    def __init__(self):
        self.contactos = {}

    def menu(self):
        opcion = 0
        while opcion != 5:
            print('1 - Carga contactos en agenda')
            print('2 - Lista contactos de agneda')
            print('3 - Consulta ingresando el nombre')
            print('4 - Modifica su teléfono y mail')
            print('5 - Finalizar programa')
            opcion = int(input('Ingrese su opción: '))
            if opcion == 1:
                self.carga()
            elif opcion == 2:
                self.lista()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificar()

    def carga(self):
        nombre = input('Ingrese el nombre')
        telefono = input('Ingrese el teléfono')
        mail = input('Ingrese el mail')
        self.contactos[nombre]=(telefono,mail)

    def lista(self):
        print('La lista es: ')
        for nombre in self.contactos:
            print(nombre,self.contactos[nombre][0],self.contactos[nombre][1])

agen = agenda()
agen1 = agenda()
agen.menu()
