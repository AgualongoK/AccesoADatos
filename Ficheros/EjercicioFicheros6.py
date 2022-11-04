'''
Ejercicio:
Escribe un programa que pida por teclado un numero positivo entre 1 y 
10 y guarde en un fichero llamado "ejercicio2-tabla.txt" la tabla de 
multiplicar (sin contar el 0) del numero introducido
Ejemplo tras introduci el numero 9:
9x1=9
9x2=18
.
.
9x10=90
'''

numero = int(input('Introduce un numero entero entre 1 y 10'))

nombre_fichero = "ejercicio2-tabla.txt"

with open(nombre_fichero, 'w') as f:

    for i in range(1,11):
            resultado = numero * i
            f.write(str(numero) + "x" + str(i) + "=" + str(resultado) + "\n")
f.close()