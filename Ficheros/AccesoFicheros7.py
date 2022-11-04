#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Creamos un archivo
f= open("archivotext-excepciones.txt","w")

#Escribimos en el
f.write("Probando excepciones")

#Cerramos el archivo
f.close()

#Ahora intentamos abrilo e imprimir su contenido
nombre_fichero="archivotext-excepciones2.txt"
try:
    with open(nombre_fichero,'r') as f:
        print(f.read())
except FileNotFoundError:
        print('No existe el fichero')