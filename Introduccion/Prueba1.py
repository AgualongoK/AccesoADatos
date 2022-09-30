print ("Hola Mundo, estoy programando en Python!")

print("""
hdeh
jdjfe
dnfdj
ajd
sjd
sw
"""
)

#Listas-> arrays dinámicos
objetos = ["casa","coche","libro"]
print(objetos)
print(objetos[1])

objetos.append("reloj")
print(objetos)

objetos.extend("curso de informatica")
print(objetos)

objetos.insert(3,"cohete")
print(objetos)

#Listas-> arrays estáticos
nombres = ("Ricardo","Maria","Laura")
print(nombres)
print(nombres[2])

num1= 2
num2 = 3

if num1 == num2 : 
    print("son iguales")
elif num1 != num2 :
    print("no son iguales")
else :
    print("Error")

"""
fnuhfdhfhdfhshfd
dfdjfdhf
iweoqiueqwe
poejje

"""

print("texto despues de un comentario de bloque")

anio =  int(input("dime un anio"))
print(anio)

#Ejercicio de pedir dos anios y compararlos.
#Si la diferecencia es mas que 100 anios: esto es mayor que un siglo
#Si la diferencia es menor a 100: esto es menor que un siglo

anio1 = int(input("dime un anio"))
anio2 = int(input("dime un anio"))

if (anio1 - anio2) > 100 : 
    print("La diferencia es mayor que un siglo")
elif (anio1 - anio2) < 100 :
    print("La diferencia es menor que un siglo")
else : 
    print("Errod de comparacion")
