#!/usr/bin/env python

# -*- coding: utf-8 -*-

with open ("archivotext3.txt","r") as f: #abrir el fichero en modo lectura
    texto=(linea for i, linea in enumerate(f) if i>=0 and i<=3)
    for linea in texto:
        print(linea)
