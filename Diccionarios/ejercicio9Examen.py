#EJERCICIO 9

def consulta_Errores(file2):
    try:
        with open(file2,"r") as f:
            print(f.readlines())
    except FileNotFoundError:
        print("El fichero no existe: ausencia de errores en la trayectoria")

def existe_Error(file1, file2):
    try:   
        f = open(file1,"r")
        f2 = open(file2,"r")
    except FileNotFoundError:
         print('No se ha encontrado el fichero')

    else:
        directorio = f.readlines()
        f.close()
        directorio2 = f2.readlines()
        f2.close()

        directorio = dict([tuple(line.split(',')) for line in directorio])
        directorio2 = dict([tuple(line2.split(',')) for line2 in directorio2])
        
    
    # Recorro las tuplas de cada diccionario y compruebo si son iguales, ya que si coincide, existiran en el fichero de control
        for i in directorio:
            for i2 in directorio2:
                if i == i2:
                    print("Datos del fichero desvio encontrados en el fichero de control " + str(i))

def borrar_Errores(file1, file2):
    try:   
        f = open(file1,"r")
        f2 = open(file2,"r")
    except FileNotFoundError:
         print('No se ha encontrado el fichero')

    else:
        directorio = f.readlines()
        f.close()
        directorio2 = f2.readlines()
        f2.close()

        directorio = dict([tuple(line.split(',')) for line in directorio])
        directorio2 = dict([tuple(line2.split(',')) for line2 in directorio2])
        
    
    # Recorro las tuplas de cada diccionario y compruebo si son iguales, ya que si coincide, existiran en el fichero de control

    try:
        for i in directorio:
            for i2 in directorio2:
                if i == i2:
                    errores = (i2)
        
        del directorio[errores]

    except:
        print("No se han borrado los errores")

def menu():
    print(
        "------MENU------" + "\n" + 
        "1.- Consultar errores" + "\n" + 
        "2.- Comprobar si existen errores entre el fichero de control y el de desvio" + "\n" + 
        "3.- Borrar errores" + "\n" + 
        "4.- Salir"
    )

def inicio():
    menu()
    fichero1 = "ficheroexam3.txt"
    fichero2 = "ficheroexam4.txt"

    while True:
        try:
            opcion = int(input("Introduzca la opción a realizar: "))

            if opcion == 1:
                consulta_Errores(fichero2)
            elif opcion == 2:
                existe_Error(fichero1,fichero2)
            elif opcion == 3:
                borrar_Errores(fichero1,fichero2)
            else:
                break
        except ValueError:
            print("Ha pulsado una tecla, por favor introduzca un numero")

inicio()