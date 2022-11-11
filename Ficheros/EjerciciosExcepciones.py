#Comentario: unicamente he incluido los ejercicios que requerian de tratar la excepcion
#Ejercicio 1
'''
Escribir un programa que lea un numero n por teclado y a
partir de ese numero, lea las n pimeras lineas del fichero creado en el ejercicio 
ficheros 6

try:
    numero = int(input("Escribe un numero de lineas:"))
    with open ("ejercicio2-tabla.txt","r") as f:
        texto=(linea for i, linea in enumerate(f) if i>-1 and i<numero)
        for linea in texto:
            print(linea)
    f.close()
except FileNotFoundError:
    print('El fichero no existe')
'''
#Ejercicio 2
'''
Escribe un programa que pida un numero entero positivo entre 1 y 10,
y en base al numero leido, busque el fichero llamado: "fichero-tabla-del-n.txt"
Este fichero contendra la tabla de multiplicar del numero introducido por teclado
y debera mostrarse por pantalla. Si el fichero no existe, debera indicarse
por partalla un mensaje que avise del problema.

n = int(input("Escribe un numero del 1 al 10"))

try:
    with open("fichero-tabla-del-" + str(n) + ".txt", "r+") as f:
     f.write("Tabla del " + str(n) + ":" + "\n")
     for i in range(1,11):
            f.write(str(n) + "x" + str(i) + "=" + str(n*i) + "\n")
    f.close()
except FileNotFoundError:
    print("Fichero no encontrado")
'''
#Ejercicio 3
'''
Escribe un programa que pida por teclado un numero positivo entre 1 y 
10 y guarde en un fichero llamado "ejercicio3-tabla.txt" las tablas de 
multiplicar de todos los numeros introducidos desde el 1 hasta el numero
elegido. Cada tabla debera estar identificada mediante un texto en pantalla:
Tabla del 1:
1x0=0
1x1=1
.
.
Tabla del 2:
etc

try:
    numero = int(input('Introduce un numero entero entre 1 y 10'))

    with open("ejercicio9-tabla.txt", 'w') as f:

     for indice in range(1, (numero+1)):
        f.write("\n" + "Tabla del " + str(indice) + "\n")
        for e in range(0,11):
                f.write(str(indice) + "x" + str(e) + "=" + str(indice*e) + "\n")
    f.close()
except FileNotFoundError:
    print('El fichero no existe')
'''
