"""
# Sentencia While
i=0
while(i<=9):
    i +=1
    print("Este while incrementa un contador: ",i)
    
while True:
    opcion = (input(""" """Que quieres de desayuno:
        1. churros con chocolate
        2. tostada con zumo
        3. tortilla de patata
        4. pizza fria
        5. ayuno intermitente
        6. salir"""
"""  
"""

# Ejercicio: realizar la calculadora junto con un menu
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

opcion = 0
def dameNumeros():
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce un numero: "))
    return(num1,num2)
       
while (opcion!=7):
    opcion = int(input("""
        "Introduce la opcion que quieres realizar: 
        1.Sumar
        2.Restar
        3.Multiplicar
        4.Dividir
        5.Exponente
        6.Verificar pares
        7.Salir"""))
    
    if opcion == 1:
        a,b = dameNumeros()
        sumar(a,b)
    if opcion == 2:
        a,b = dameNumeros()
        restar(a,b)
    if opcion == 3:
        a,b = dameNumeros()
        multiplicar(a,b)
    if opcion == 4:
        a,b = dameNumeros()
        dividir(a,b)
    if opcion == 5:
        a,b = dameNumeros()
        exponente(a,b)
    if opcion == 6:
        a,b = dameNumeros()
        numerosPares(a,b)
        
