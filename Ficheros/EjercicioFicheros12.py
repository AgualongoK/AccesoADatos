#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio2:
Escribe un programa que pida por teclado un numero positivo entre
1 y 10 y guarde en un fichero llamado "ejercicio2_2-tabla.txt." la tabla
de multiplicar del numero introducido
Ejemplo tras introducir el nº9
9x1=9
9x2=18
...
...
9x10=90
'''

num = int(input("Introduce un numero entre 1 y 10"))

nombre_fichero = "ejercicio2_2-tabla.txt"
with open(nombre_fichero, "w") as f:
    for i in range(11):
     f.write(str(num) + 'x' + str(i) + '=' + str(num*i) + '\n')
f.close()