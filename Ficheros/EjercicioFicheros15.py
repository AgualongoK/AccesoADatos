#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un programa en python que lea un numero n por teclado
y a partir de ese numero, lea las n primeras lineas del fichero creado
en el ejercicio 2
'''

num = int(input("Escribe un numero del 1 al 11:"))

with open("ejercicio2_2-tabla.txt","r") as f:
    for i in range(num):
        print(f.readline())
f.close()