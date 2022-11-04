#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio: escribir x veces un texto en el fichero
with open("ficheroenpython.txt", "r+") as f: 
    contenido = f.read()
    for i in range(8):
        f.write("\n Opcion ")
f.close()