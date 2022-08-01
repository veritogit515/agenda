from db import connect,create_db, update_data, insert_data, delete_data, get_all_data, get_data, delete_data

#Creamos la clase Agenda


class Agenda():

    #Definir el Constructor
    def __init__(self):
        self.contactos = []
        connect()
        create_db()

    def menu(self):
        print()
        menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto', "anadir"],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Eliminar contacto'],
            ['6. Cerrar agenda']
        ]

        for x in range(7):
            print(menu[x][0])
        
        opcionseleccionada = int(input("Ingrese el numero de la accion que desea realizar:"))

        if opcionseleccionada == 1:
            self.anadir()
        elif opcionseleccionada == 2:
            self.listar()
        elif opcionseleccionada == 3:
            print("Buscar contactos")
            print('------------------------')
            nombre = input("Introduzca el nombre a buscar")
            get_data(nombre)
        elif opcionseleccionada == 4:
            self.editar()
        elif opcionseleccionada == 5:
            self.eliminar()
        elif opcionseleccionada == 6:
            print("Saliendo de la Agenda...")
            exit()
            
        # Volvemos a llamar a Menu para que se ejecute
        self.menu()

    #Añadir un contacto
    def anadir(self):
        print("Añadir nuevo contacto")
        print('------------------------')
        nombre = input("Ingrese el nombre:\n")
        apellido = input("Ingrese el apellido:\n")
        telefono = input("Ingrese el telefono:\n")
        mail = input("Ingrese el mail:\n")
        #self.contactos.append({'nombre': nom, 'telf': telf, 'email': email})
        insert_data(nombre,apellido, telefono, mail)

    #Listar contactos

    def listar(self):
        print("Listar contactos")
        print('------------------------')
        get_all_data()

    # Editar/Actualizar contacto
    def editar(self):
        print("Actualizar datos de contacto")
        print('------------------------')
        nom_buscado=input("Introduzca el nombre a buscar")
        get_data(nom_buscado)
        print("A continuación solicitaremos que introduzca los datos para actualizarlos")
        nombre = input("Introduzca el nuevo nombre:")
        apellido = input("Introduzca el nuevo apellido:")
        telefono = input("Introduzca el nuevo telefono:")
        mail = input("Introduzca el nuevo mail:")
        update_data(nom_buscado, nombre, apellido, telefono,mail)

    # Eliminar un contacto
    def eliminar(self):
        print("Eliminar datos de contacto")
        print('------------------------')
        nom_buscado=input("Introduzca el nombre a buscar")
        get_data(nom_buscado)
        delete_data(nom_buscado)


     

agenda = Agenda()
agenda.menu()






