#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escribir al final de un fichero
with open("ficheroenpython.txt", "r+") as f: #Abrimos el fichero utilizando Reescribir (r+)
    contenido = f.read()
    #Escribimos la nueva linea
    f.write("\nEscribiendo una nueva linea al final")
f.close()

#Otra manera de escribir al final de un fichero
with open("ficheroenpython.txt", "a") as f: 
    f.write("\nEscribiendo una nueva linea al final con a")
f.close()

#Escibir al principio de un fichero  sobreescribiendo su contenido
with open("ficheroenpython.txt", "r+") as f: #Abrimos el fichero utilizando Reescribir (r+)
    #Escribimos la nueva linea
    f.write("Escribiendo una nueva linea al principio \n")
f.close()

