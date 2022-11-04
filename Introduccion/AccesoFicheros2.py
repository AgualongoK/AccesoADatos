#!/usr/bin/env python

# -*- coding: utf-8 -*-

#forma clasica de crear un archivo:

#Creamos el archivo
with open("archivotext.txt","w") as f:

#Escribimos en el
    f.write("Creando archivo de texto en python with as")

#Cerramos el archivo
f.close()