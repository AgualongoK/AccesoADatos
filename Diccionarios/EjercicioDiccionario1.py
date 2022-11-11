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