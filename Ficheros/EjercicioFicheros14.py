#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribe un programa que pida un numero entero positivo n entre 1 y 10,
y en base al numeor leido, busque el fichero llamado:
"fichero-tabla-del-n.txt". Este fichero contendra la tabla de multiplicar
del numero n introducido x teclado y debera mostrarse x pantalla.
Si el fichero no existe, debera indicarse x pantalla un mensaje que
avise del problema
'''

num = int(input("Introduce un numero del 1 al 10"))

nombre_fichero = "fichero-tabla-del-" + str(num) + ".txt"

try:
    with open(nombre_fichero,"r") as f:
        print(f.read())
        f.close
except FileNotFoundError:
    print("No existe el fichero")