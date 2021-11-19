class Contacto():
    def __init__(self,nombre,telefono,email):
        self.nombre= nombre
        self.telefono = telefono
        self.email= email

    def __str__(self):
        return (f"""Nombre: {self.nombre}
Telefono: {self.telefono}
Email: {self.email}""")




class Agenda():
    def __init__(self):
        self.contactos = []

    def aniadir(self):
        self.nombre = (input("Ingrese el nombre de contacto: "))
        self.telefono = int(input("Ingrese el telefono: "))
        self.email = (input("Ingrese el email: "))
        self.contactos.append(Contacto(self.nombre,self.telefono,self.email))

    def editar(self):
        
        
        data = self.contactos[self.buscar()]
        while  True:
            print("EDITAR")
            print("1-Editar nombre:")
            print("2-Editar telefono:")
            print("3-Editar email:")
            print("4-Cerrar")
            opcion = int(input("Seleccionar la opcion"))
            if opcion == 1:
                nombreEditar = input("Ingrese nombre a editar ")
                data.nombre = nombreEditar
            elif opcion == 2:
                telefonoEditar = input("Ingrese nuevo numero ")
                data.telefono = telefonoEditar
            elif opcion == 3:
                emailEditar = input("Ingrese mail a editar ")
                data.email = emailEditar
            elif opcion == 4:
                break
        
    
    def mostrarLista(self):
        if len(self.contactos) == 0:
            print("No hay contactos guardados.")
        else:
            for i in (self.contactos):
                print(i.nombre,i.telefono,i.email)
    
    def buscar(self):
        nombreContacto = input("Ingrese el nombre del contacto buscado")
        for c,i in enumerate(self.contactos):
            if nombreContacto == i.nombre:
                print("Nombre:",i.nombre)
                print("Telefono:",i.telefono)
                print("Email:",i.email)
        return(c)
    
    def eliminarContacto(self):
        del self.contactos[self.buscar()]


class Menu:
    def __init__(self):
        
        self.agenda = Agenda()
        self.mostrarMenu()
    
        
    def mostrarMenu(self):
        self.menu= [
            ['                ------ Agenda de Contactos------'],
            ['                |      1- Añadir Contacto      |'],
            ['                |      2- Lista Contacto       |'],
            ['                |      3- Buscar Contacto      |'],
            ['                |      4- Editar Contacto      |'],
            ['                |      5- Eliminar Contacto      |'],
            ['                |      6- Cerrar Agenda        |'],
            ['                --------------------------------']
        ]
        
        
        while True:
            for i in range(8):
                print(self.menu[i][0])
            opcion = int(input("Ingrese la opcion que desea ejecutar. "))
            if opcion == 1:
                self.agenda.aniadir()
            elif opcion == 2:
                self.agenda.mostrarLista()
            elif opcion == 3:
                self.agenda.buscar()
            elif opcion == 4:
                self.agenda.editar()
            elif opcion == 5:
                self.agenda.eliminarContacto()
            elif opcion == 6:
                print("Cerrando agenda...")
                exit()
            
    
menu=Menu()



