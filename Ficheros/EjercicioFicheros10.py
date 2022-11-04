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
