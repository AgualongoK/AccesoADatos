'''
Ejercicio:
Escribir un programa que le un numero n por teclado y a
partir de ese numero, lea las n pimeras lineas del fichero creado en el ejercicio 
ficheros 6
'''

numero = int(input("Escribe un numero de:"))

with open ("ejercicio2-tabla.txt","r") as f:
    for i in range(numero):
        print(f.readline())
f.close()

# Opcion 2
#!/usr/bin/env python
# -*- coding: utf-8 -*-
numero = int(input("Escribe un numero de:"))
with open ("ejercicio2-tabla.txt","r") as f:
    texto=(linea for i, linea in enumerate(f) if i>0 and i<numero)
    for linea in texto:
        print(linea)
f.close()