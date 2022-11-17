def textoMenu(): 
    print("----- Agenda telefonica ----- \n" + 
        "1. Crear fichero \n" + 
        "2. Aniadir contacto \n" + 
        "3. Consultar telefono \n" + 
        "4. Borrar contacto \n" +
        "5. Salir")

def crearFichero(): 
    try:
        with open("miAgenda20.txt","w") as f:
            f.close
    except FileExistsError:
        respuesta = str(input("El fichero ya existe, desea borrar su contenido? s/n"))
        if respuesta.lower == "s":
            with open("miAgendia.txt","w+") as f:
                f.write("")
                f.close()
        else:
            opcion = 0
    except FileNotFoundError:
        respuesta = str(input("No se ha encontrado el fichero, desea crearlo? s/n"))
        if respuesta.lower == "s":
            with open("miAgenda.txt","w") as f:
                f.xlose()
        else:
            print("El fichero ya existe")

def aniadirContacto():
    nombre = str(input("Introduzca el nombre del contacto a aniadir:"))
    numeroTelefono = int(input("Introduzca el numero de telefono a aniadir:"))
    with open("miAgenda.txt","r+") as f:
        f.write(nombre + "," + str(numeroTelefono))
        f.close()
    print("Contacto aniadido exitosamente")

def consultarTelefono():
    numeroTelefono = int(input("Introduzca el numero de telefono a consultar"))
    with open("miAgenda.txt","r") as f:

        if f.readlines().__contains__(str(numeroTelefono)) : 
            resultadoBusqueda = f.readlines().__contains__(str(numeroTelefono))
            print(resultadoBusqueda)
        else:
            print("No se ha encontrado el contacto")

def borrarContacto(nombreContacto):
    with open("miAgenda.txt","r") as f:
       contenido = f.readlines()
    with open("miAgenda.txt","w") as f2:
        for lineas in f:
            if nombreContacto not in lineas:
                f2.write("")
    f2.close()
    f.close()


opcion = 0
salir  = False

while not salir:

    textoMenu()

    opcion = int(input("Introduzca la opcion que quiere realizar"))

    if opcion == 1:
        crearFichero()
    if opcion == 2:
        aniadirContacto()
    if opcion == 3:
        consultarTelefono()
    if opcion == 4:
        borrarContacto()
        salir()
    if opcion == 5:
        salir = True
    else:
        print("Opcion incorrecta. Por favor, introduzca una opcion valida")

print("----- Cerrando agenda telefonica ------")