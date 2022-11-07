'''
Ejercicio 1: 
Escribe un programa que pida por teclado un numero positivo entre 1 y 100
y lo guarde en un fichero llamado "ejercicio1-10.txt"
'''

# str() -> lo que admite el fichero.txt

print("Escribe un numero entre 1 y 100")
numero = input()

f = open("ejercicio1-100.txt","w") 
f.write(numero)
f.close()


'''
Opcion formal:

n = int(input('Introduce un numero entero entre 1 y 100: '))
nombre_fichero = 'ejercicio1-100.txt'
with open(nombre_fichero, 'w') as f:
    f.write(str(n))
f.close()
'''