#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ampliar el diccionario de abajo con los siguientes campos.Ponerlos en codigo
1*Apellido, edad 18, genero, padres(james, lili)
2*Si lo que queremos es imprimir por pantalla el diccionario
3*Si lo que queremos es imprimir el valor de una clave
4*Si lo que queremos es acceder a una clave concreta dentro de un campo
5*Cambiar la edad a 22
6*Aniadir un campo Grupo nuevo al final
7*Cambiar el nombre de una clave por otro. Por ejemplo cambiar la clave Grupo por la Casa
sin necesidad de usar for para recorrer la clave ni el diccionario
8*Borrar un par clave-valor
'''

#1
MiDiccionario = {
    'Nombre' : "Harry",
    'Apellido' : "Potter",
    'Edad' : 18,
    'Genero' : "Masculino",
    'Padres' : ['James','Lili']
}

#2
print(MiDiccionario)

#3
print(MiDiccionario['Apellido'])

#4
print(MiDiccionario["Padres"][0:2])

#dime el Valor del segundo elemento de mi diccionario del campo padres
print(MiDiccionario["Padres"][1])
print(MiDiccionario["Padres"][1:2])

#5
MiDiccionario["Edad"] = 22
print(MiDiccionario["Edad"])

#6
MiDiccionario["Grupo"] = "Gryffindor"
print(MiDiccionario)

#7
MiDiccionario["Casa"]=MiDiccionario.pop("Grupo")

#8
del MiDiccionario["Edad"]
print(MiDiccionario)

#9 dos formas de obtener el valor de una clave
print(MiDiccionario['Apellido']) # forma 1 
print(MiDiccionario.get('Apellido')) # forma 2 con get

#10 aniadir a una variable el valor de una clave
valorVariable = MiDiccionario.get("Nombre")
print(valorVariable)

# 11 Imprimir las claves del diccionario: .keys()
print(MiDiccionario.keys())

# 12 Imprimir todos los valores: .value
print(MiDiccionario.values())

# TUPLAS

# 13 Crear una tupla: ()
Cosas =  ("casa", "puerta", "reloj", "mesa", "silla", "banco", "cuadro", "alfombra")

Numeros = (1,2,3,4,5)

# 14 como ver el par (clave-valor) de un diccionario; devuelve una tupla
print("\n\n --------------")
print(MiDiccionario.items())

# 15 Crear una tupla
Numeros2 = (111,222,333,444,555,666)
#15 Slice: vamos a imprimir partes (rebanadas) de una tupla y vamos 
# a seleccionar (imprimir) los tres primeros elementos de la tupla
print(Numeros2[0:3])
print(Numeros2[1:3])
print(Numeros2[:-3])
print(Numeros2[-2:])

#16 como saber la longitud de un diccionario
print("\n\n ----Longitud diccionario ----")
print(len(MiDiccionario))

#17 como saber la longitud de una clave de un diccionario`
# quiero saber la longitud de la clave padres, es decir
# cuantos elementos contiene esa clave, que deberian ser 2
print("\n\n ----Longitud de una clave de un diccionario")
print(len(MiDiccionario["Padres"]))

#18 SPLIT
print("\n\n ---Split----")
text = "Partiendo con split"
print(text.split())

#19 
'''
Escribe el siguiente texto y partelo
Python es un lenguaje de programacion que permite tipar pero
no permite compilar, ya que es un lenguaje interpretado

19a: cogiendo las comas como separador
19.b: cogiendo los espacios en blanco
19.c: cogiendo la letra 'e'
''' 

text2 = "Python es un lenguaje de programacion que permite tipar pero no permite compilar, ya que es un lenguaje interpretado"
print(text2.split(','))
print(text2.split(' '))
print(text2.split('e'))

'''
20 Crea un programa que a partir del fichero de "prueba1.txt" el cual contiene exactamente esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura y para cada line del fichero, imprima
20.a) el contenido de la linea
20b) el contenido de cada linea desglosado por caracteres:
    ('A',',','1,'\n)
20.c) El contenido de cada linea en formato 'primer elemtno', 'segundo elemento' o lo que
es lo mismo, clave-valor:
    ('A','1'\n)
'''
print("---- Ejercicio 20 ----")

with open("prueba1.txt", "r") as f:
    for i in range(len("prueba1.txt")):
        print(f.readline())
f.close()

print("\n\n --- TUPLEANDO ---")
mitupla = tuple([1,4,6])
print(mitupla)

mitupla2=tuple("texto")
print(mitupla2)

mitupla3=tuple({4:'one', 6:'two'})
print(mitupla3)
print(mitupla3[0])

#como crear un diccionario directamente: dic
midic2=dict(nombre="lm", altura=195, ojos='azules')
print(midic2)

'''
Pasos a seguir para el eje.20
-abrir el fichero en modo lectura
-guardar el contenido del fichero en una variable
-cerrar el fichero
-iterar sobre el contenido cada linea
-imprimir lo que se pide
    a:cada linea
    b:tuplear
    c:tuplear
'''

print("\n\n\n\n")
file="prueba1.txt"
f=open(file,'r')
contenido = f.readlines()
f.close()

line = str()
for line in contenido:
    print("el contenido de cada linea es:" , line)
    print(tuple(line))
    print(tuple(line.split(',')))

'''
21
20 Crea un programa que a partir del fichero de "prueba1.txt" el cual contiene exactamente esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura y para cada linea del fichero e indique si una letra introducida
por teclado está dentro del fichero, y de estarlo, qué valor tiene asociado
En caso de no estar la letra introducida, mostrará un mensaje indicando:
"la letra leida" ; "la letra leída no se encuentra en el fichero"
'''

print("\n\n\n\n")

print("----- EJERCICIO 21 ----- ")
letra = str(input("Introduzca a la letra a buscar"))

with open ("prueba1.txt", "r") as f:
      contenidofichero = f.readline()
      for line in contenidofichero:
        if letra in line:
            print("letra encontrada")
            print(letra)
            break
        else:
            print("letra no encontrada")
            break
f.close()
