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
MiDiccionario["Grupo"] = ""
print(MiDiccionario)

#7
MiDiccionario["Casa"]=MiDiccionario.pop("Grupo")
