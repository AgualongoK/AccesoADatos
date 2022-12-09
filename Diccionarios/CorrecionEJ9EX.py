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