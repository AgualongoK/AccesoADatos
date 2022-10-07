"""
print ("Hola Mundo, estoy programando en Python!")

print("""
"""
hdeh
jdjfe
dnfdj
ajd
sjd
sw
"""
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

fnuhfdhfhdfhshfd
dfdjfdhf
iweoqiueqwe
poejje


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
    print("Error de comparacion")


#Ejemplo de un for
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    

#Ejercicio que simule un menu y el usuario introduzca su opcion


opcion = int(input("Selecciona lo que quieres imprimir: 1Pares 2Impares 3Ambos"))

if opcion == 1 :
    print("Numeros pares: ")
    for num in numeros : 
        if num % 2 == 0 : 
            print(num)
elif opcion == 2 : 
    print("Numeros impares: ")
    for num in numeros : 
        if num % 2 != 0 : 
            print(num)
elif opcion == 3 :
    print("Numeros pares e impares")
    for num in numeros : 
        if num % 2 == 0 : 
             print(num)
    for num in numeros : 
        if num % 2 != 0 : 
             print(num)
else : 
    print("Opcion no disponible")


palabras = ['Peine','Pelo','Ventana','Refrigerador','Adolescente','Dentista','Asesino']
for caracteres in palabras:
    print((caracteres),(len (caracteres)))



# Declarar una lista con una frase, recorrer y decir cuantas 'a' hay
frase = ["Hola, estoy programando en python"]
contador = 0

for caracteres in frase:
    if "a" in caracteres :
        contador = contador + 1
        contador += contador

print("Hay un total de " + str(contador) + " 'a'")



# Ejercicio: un programa que lea 4 numeros y muestre por pantalla el mayor
aux = 0
for i in range(4):
    m=int(input("Dame un numero: "))
    if m>aux:
        aux=m
print("El numero mayor es:", aux)

"""
# Ejercicio: programa para una empresa de salas de Juegos para todas las edades y quiere calcular de forma
# automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente
# es menor de 4 años entra gratis, entre 4 y 18 años paga 5E y si es mayor de 18 paga 10E

edad = int(input("Indique su edad"))

if edad<=4:
        print("Entrada gratuita")
if edad>4 and edad<=18:
        print("Entrada 5€")
if edad > 18:
        print("Entrada 10€")