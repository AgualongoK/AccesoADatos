#EJERCICIO 5
'''
while True: 
    try: 
        opcion=int(input("Introduce una opción del 1 al 3:"))

        if opcion == 1:
            print("opcion 1")
        elif opcion==2:
            print("opcion 2")
        elif opcion==3:
            print("opcion 3")
        else:
            break
    except ValueError:
        print("Ha pulsado una tecla, por favor introduzca un número")
'''

#EJERCICIO 6
'''
nombre = str(input("Introduce un nombre: "))
apellido = str(input("Introduce un apellido: "))
edad = int(input("Introduce una edad: "))
telefono = int(input("Introduce un telefono: "))

miDiccionario = {
    'Nombre' : nombre ,
    'Apellido' : apellido,
    'Edad' : edad,
    'Telefono' : telefono
}

print(nombre + " tiene " + str(edad) + " anios y su telefono es " + str(telefono))
#print(miDiccionario)
'''

#EJERCICIO 7-a
'''
numero = int(input("Introduce un numero mayor a 0: "))

with open ("ficheroexam1.txt","w") as f:
    for i in range(numero+1):
     f.write("El numero es: " + str(i) + "\n")
f.close()
'''

#EJERCICIO 7-b
'''
numero = int(input("Introduce un numero mayor a 0: "))

with open ("ficheroexam1.txt","a") as f:
    f.write("--------- \n")
    for i in range(numero+1):
     f.write("El numero es: " + str(i) + "\n")
f.close()
'''

#EJERCICIO 8-a
'''
#funcion para realizar el calculo de la operacion solicitada
def calculo(numero1,numero2,numero3):
    resultado = (numero1+numero2) * numero3
    return resultado

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))

with open ("ficheroexam2.txt","w") as f:
    # almaceno el resultado en una variable para poder incluirlo como rango en el for
    resultadoDef = calculo(num1,num2,num3)
    for i in range(resultadoDef):
        f.write("El resultado es: " + str(resultadoDef) + " y esta es la linea: " + str(i+1) + "\n")
f.close()
'''

#EJERCICIO 8-b
'''
#funcion para realizar la suma de los numeros
def calculo2(numero1,numero2):
    suma = numero1+numero2
    return suma

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))

with open("ficheroexam2.txt","r") as f:
     #almacenamos el resultado de la suma en una variable que equivaldra al numero de lineas
    resultadoDef2 = calculo2(num1,num2)
    for i in range(resultadoDef2):
        print(f.readline())
f.close()
'''

#EJERCICIO 8-c
'''
#funcion para realizar la suma de los numeros
def calculo2(numero1,numero2):
    suma = numero1+numero2
    return suma

try:
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce un numero: "))
    nombreFichero = "ficheroexam2.txt"

    with open(nombreFichero,"r") as f:
         #almacenamos el resultado de la suma en una variable que equivaldra al numero de lineas
        resultadoDef2 = calculo2(num1,num2)
        for i in range(resultadoDef2):
            print(f.readline())
    f.close()

except FileNotFoundError:
    print("El fichero" + nombreFichero + " no existe!")
'''

#EJERCICIO 9
'''
def consulta_Errores(file2):
    try:
        with open(file2,"r") as f:
            print(f.readlines())
    except FileNotFoundError:
        print("El fichero no existe: ausencia de errores en la trayectoria")

def existe_Error(file1, file2):
    try:   
        f = open(file1,"r")
        f2 = open(file2,"r")
    except FileNotFoundError:
         print('No se ha encontrado el fichero')

    else:
        directorio = f.readlines()
        f.close()
        directorio2 = f2.readlines()
        f2.close()

        directorio = dict([tuple(line.split(',')) for line in directorio])
        directorio2 = dict([tuple(line2.split(',')) for line2 in directorio2])
        
    
    # Recorro las tuplas de cada diccionario y compruebo si son iguales, ya que si coincide, existiran en el fichero de control
        for i in directorio:
            for i2 in directorio2:
                if i == i2:
                    print("Datos del fichero desvio encontrados en el fichero de control " + str(i))

def borrar_Errores(file1, file2):
    try:   
        f = open(file1,"r")
        f2 = open(file2,"r")
    except FileNotFoundError:
         print('No se ha encontrado el fichero')

    else:
        directorio = f.readlines()
        f.close()
        directorio2 = f2.readlines()
        f2.close()

        directorio = dict([tuple(line.split(',')) for line in directorio])
        directorio2 = dict([tuple(line2.split(',')) for line2 in directorio2])
        
    
    # Recorro las tuplas de cada diccionario y compruebo si son iguales, ya que si coincide, existiran en el fichero de control

    try:
        for i in directorio:
            for i2 in directorio2:
                if i == i2:
                    errores = (i2)
        
        del directorio[errores]

    except:
        print("No se han borrado los errores")

def menu():
    print(
        "------MENU------" + "\n" + 
        "1.- Consultar errores" + "\n" + 
        "2.- Comprobar si existen errores entre el fichero de control y el de desvio" + "\n" + 
        "3.- Borrar errores" + "\n" + 
        "4.- Salir"
    )

def inicio():
    menu()
    fichero1 = "ficheroexam3.txt"
    fichero2 = "ficheroexam4.txt"

    while True:
        try:
            opcion = int(input("Introduzca la opción a realizar: "))

            if opcion == 1:
                consulta_Errores(fichero2)
            elif opcion == 2:
                existe_Error(fichero1,fichero2)
            elif opcion == 3:
                borrar_Errores(fichero1,fichero2)
            else:
                break
        except ValueError:
            print("Ha pulsado una tecla, por favor introduzca un numero")

inicio()

'''