"""
def sumar(a,b):
    print("La suma de los numeros es: ", a+b)

sumar(4,7)
    
"""

# Ejercicio: escribir las funciones suma, resta, multiplicacion, dividir, exponerte y otra que te inventes
# Pedir por teclado los numeros y que te muestre por pantalla todas las operaciones
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))

def sumar(a,b):
    print("El resultado de la suma es: ", a+b)
def restar(c,d):
    print("El resultado de la resta es: ", c-d)
def multiplicar(e,f):
    print("El resultado de la multiplicacion es: ", e*f)
def dividir(g,h):
    print("El resultado de la division es: ", g/h)
def exponente(i,j):
    print("El resultado de elevar el primer numero al segundo numero es: ", i**j)
def numerosPares(k,l):
    if k % 2 == 0 or l % 2 == 0:
        print("Hay un numero par entre los introducidos")
    else:
        print("No hay numeros pares entre los introducidos")
        
sumar(num1,num2)
restar(num1,num2)
multiplicar(num1,num2)
dividir(num1,num2)
exponente(num1,num2)
numerosPares(num1,num2)
