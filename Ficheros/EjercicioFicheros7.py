'''
Ejercicio:
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
'''
numero = int(input('Introduce un numero entero entre 1 y 10'))

with open("ejercicio3-tabla.txt", 'w') as f:

    for indice in range(1, (numero+1)):
        f.write("\n" + "Tabla del " + str(indice) + "\n")
        for e in range(0,11):
                f.write(str(indice) + "x" + str(e) + "=" + str(indice*e) + "\n")
f.close()