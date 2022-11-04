#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("ficheroenpython.txt", "r+") as f: #Abrimos el fichero utilizando Reescribir (r+)
    contenido = f.read()
    #Escribimos la nueva linea
    f.write("\nEscribiendo una nueva linea al final")
f.close()