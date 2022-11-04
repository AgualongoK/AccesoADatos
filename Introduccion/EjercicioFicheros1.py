'''
Escribe un programa en python que escriba de la forma clasica en un 
fichero llamado "ficheroenpython.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en python usando 
la forma clásica, que es la siguiente:
f = open()
f.write()
f.close()
'''

f = open("ficheroenpython.txt","w")

f.write("Este es mi primer programa de fichero y lo he escrito en python usando la forma clasica, que es la siguiente: \n f = open() \n f.write() \n f.close()")

f.close()