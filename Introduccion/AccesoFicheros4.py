#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Abrimos usando Read (r)
with open("ficheroenpython.txt", "r") as f:
    #Lo abrimos utilizando el metodo readlines() y lo almacenamos en una variable
    contenido = f.readlines() #lee todas las lineas y las separa con un \n

    #Imprimimos la variable que tiene el contenido
    print(contenido)