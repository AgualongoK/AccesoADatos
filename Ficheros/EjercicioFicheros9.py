'''
Ejercicio:
Escribe un programa que pida un numero entero positivo entre 1 y 10,
y en base al numero leido, busque el fichero llamado: "fichero-tabla-del-n.txt"
Este fichero contendra la tabla de multiplicar del numero introducido por teclado
y debera mostrarse por pantalla. Si el fichero no existe, debera indicarse
por partalla un mensaje que avise del problema.
'''

n = int(input("Escribe un numero del 1 al 10"))

try:
    with open("fichero-tabla-del-" + str(n) + ".txt", "r+") as f:
     f.write("Tabla del " + str(n) + ":" + "\n")
     for i in range(1,11):
            f.write(str(n) + "x" + str(i) + "=" + str(n*i) + "\n")
    f.close()
except FileNotFoundError:
    print("Fichero no encontrado")