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

#Opcion 2
'''
n=int(input("introduce un numero de lineas"))
with open("ejercicio2_2-tabla.txt","r") as f:
    texto = (linea for i, linea in enumerate(f) if i>0 and i<n) #enumerate cuenta lineas
    for linea in texto:
        print(linea)
f.close()
'''