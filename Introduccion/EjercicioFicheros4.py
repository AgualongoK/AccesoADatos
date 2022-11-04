#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Modificar el contenido de AccesoFicheros6 para que haga lo mismo sin usar r+
'''

Lista = ["\nEscribiendo \n", "listas \n", "en ficheros con a"]
with open("ficheroenpython.txt","a") as f:
    f.writelines(Lista)
f.close()