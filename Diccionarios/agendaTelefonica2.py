# -*- coding: utf-8 -*-
import os, sys #librerias 

# Declaro las variables del programa principal

def textoMenu(): 
    print("----- Agenda telefonica ----- \n" + 
    "1. Crear fichero \n" + 
    "2. Aniadir contacto \n" + 
    "3. Consultar telefono \n" + 
    "4. Borrar contacto \n" +
    "5. Salir")

    opcion = str(input("Introduzca la opcion que quiere realizar"))
    return opcion

def crear_fichero(file):
    '''
    Funcion que crea un fichero vacio para guardar en la agenda.
    Parametros:
        file: es un fichero que se llama 'miagenda.txt'
    Devuelve:
        un mensaje informando si el fichero se ha creado correctamente
        Ademas debe comprobar si el fichero existe o no. Y si existe, lo machaca
    '''
    # abrir, cerrar y escribir un mensaje que diga: se ha creado el fichero ...txt
    #import os Libreriapara trabajar con ficheros
    if os.path.isfile(file): #nos indica si el fichero existe o no
        answer = input('El fichero ' + file + ' ya existe. ¿Desea vaciarlo? (S/N)')
        if answer == 'N':
            return 'No se ha creado el fichero porque ya existe'
            
    f = open(file,'w')
    f.close
    return 'Se ha creado el fichero para la agenda. \n'

def lanzarPorgama():
    '''
    Funcion que lanza las opciones del menu de la aplicacion para la gestion de agenda telefonica
    '''
    fichero = "miagenda.txt"
    opcion = str()
    while True:
        opcion = textoMenu()
        print("la opcion pulsada es:", opcion)
        if opcion == '1':
            crear_fichero(fichero)
        if opcion == '2':
            print("menu2")
        if opcion == '3':
            print("menu3")
        if opcion == '4':
            print("menu4")
        else:
            break

    #return


lanzarPorgama()