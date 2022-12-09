#------- DECLARO FUNCIONES ---------
def Consulta_Errores(fichero2):
    try:
        f = open(fichero2,'r')
        directorio = f.readlines()
        f.close()
        for i in range(len(directorio)):
            print(directorio[i])
    
    # ---- Comprobar tamanio de los ficheros -----
        print('\n\n Comprobando tamanio: ')
        f = open(fichero2,'r')
        directorio = f.readlines()
        print('El fichero con datos de desvio contiene', len(directorio), ' posibles errores de trayectoria')

    except FileNotFoundError:
        print('\n El fichero ' + fichero2 + ' no existe! \n')

def Existe_Error(fichero, fichero2):
    clave1=[]
    clave2=[]
    contador=int(0)

    try:
        f = open(fichero,'r')
        g = open(fichero2,'r')
        directorio = f.readlines()
        directorio2 = g.readlines()
        f.close()
        g.close()

        #transformo el tipo de datos
        directorio = dict([tuple(line.split(',')) for line in directorio])
        directorio2 = dict([tuple(line.split(',')) for line in directorio2])
        #almaceno las llaves de ambos ficheros en unas listas, para posteriormente compararlas
        clave1 = directorio.keys()
        clave2 = directorio2.keys()

        print("clave1: datos del fichero de control:", clave1)
        print("clave2: datos del fichero de desvio:", clave2)

        for elemento in clave2:
            if str(elemento) in clave1:
                contador=contador+1
        return(contador==len(clave2))

    except FileNotFoundError:
        print('\n Comprueba que existen ambos ficheros! \n')

def Borrar_Errores(fichero, fichero2):

    clave1=[]
    clave2=[]
    contador=int(0)

    try:
        f = open(fichero,'r')
        g = open(fichero2,'r')
        directorio = f.readlines()
        directorio2 = g.readlines()
        f.close()
        g.close()

        #transformo el tipo de datos
        directorio = dict([tuple(line.split(',')) for line in directorio])
        directorio2 = dict([tuple(line.split(',')) for line in directorio2])
        #almaceno las llaves de ambos ficheros en unas listas, para posteriormente compararlas
        clave1 = directorio.keys()
        clave2 = directorio2.keys()

        print("clave1: datos del fichero de control:", clave1)
        print("clave2: datos del fichero de desvio:", clave2)

        for elemento in clave2:
            if str(elemento) in clave1:
                del clave1[elemento]
        
        f = open(fichero,'w')
        for clave1,valor1 in directorio.items():
            f.write(clave1 + ',' + valor1)
        f.close()

    except FileNotFoundError:
        print('\n Comprueba que existen ambos ficheros! \n')



def menu():
    print('\n','\n','Gestion del sistema de control de vuelo')
    print('=========================')
    print('1- Consultar coordenadas erroneas')
    print('2- Buscar el error')
    print('3- Eliminar un telefono')
    print(' - Terminar')
    opcionmenu = (input('Introduzca el numero de la opcion deseada: '))
    return opcionmenu

def inicio():
    file = 'ficheroexam3.txt'
    file2 = 'ficheroexam4.txt'

    while True:
        opcion = menu()
        if opcion == '1':
            Consulta_Errores(file2)
        elif opcion == '2':
            if Existe_Error(file, file2):
                print('Se han encontrado todos los errores')
            else:
                print('No se encontraron todos los errores')
        elif opcion == '3':
            Borrar_Errores(file, file2)
        else:
            print('Desconectando')
            print('...')
            print('..')
            print('.')
            break

#---------- PROGRAMA PRINCIPAL ------------
inicio()