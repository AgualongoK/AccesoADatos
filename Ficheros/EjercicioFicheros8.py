'''
Ejercicio:
Modifica el ejercicio ficheros 6 para que el fichero tenga el nombre del numero con
el que se crea la tabla de multiplicar. Por ejemplo, si se introduce por
teclado el 9, que el fichero se llame "ejercicio2-tabla del 9.txt"
'''

numero = int(input('Introduce un numero entero entre 1 y 10'))

nombre_fichero = "ejercicio2-tabla" + str(numero) + ".txt"

with open(nombre_fichero, 'w') as f:
    f.write("Tabla del " + str(numero) + ":" + "\n")
    for i in range(1,11):
            resultado = numero * i
            f.write(str(numero) + "x" + str(i) + "=" + str(resultado) + "\n")
f.close()