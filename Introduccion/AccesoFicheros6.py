#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escribir el contenido de un array en un fichero

Lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

#Abrimos fichero como Reescribir (r+)
with open("ficheroenpython.txt","r+") as f:
    #Abrimos lectura del fichero y lo almacenamos en una variable
    contenido = f.read()

    #Escribimos la lista en el archivo linea a linea
    f.writelines(Lista)
f.close()