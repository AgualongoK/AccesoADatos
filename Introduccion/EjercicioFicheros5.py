'''
Ejercicio: 
Escribe un programa que pida por teclado un numero positivo entre 1 y 100
y lo guarde en un fichero llamado "ejercicio1-10.txt"
'''

# str() -> lo que admite el fichero.txt

print("Escribe un numero entre 1 y 100")
numero = input()

f = open("ejercicio1-100.txt","w") 
f.write(numero)
f.close()
