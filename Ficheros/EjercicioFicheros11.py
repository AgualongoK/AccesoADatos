'''
Ejercicio1:
Escribe un programa que pida por teclado un numero entre 1 y 
100 y lo guarde en un fichero llamado "ejercicio-100.txt"
'''

num = int(input("Escribe un numero entre 1 y 100"))

with open ("ejercicio1-100.txt","w") as f:
    f.write(str(num))
f.close()