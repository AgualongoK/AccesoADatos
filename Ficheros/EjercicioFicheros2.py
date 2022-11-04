'''
Escribe un programa en python que escriba de la forma clasica en un 
fichero llamado "ficheroenpython2.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en python usando 
la forma recomendada, que es la siguiente:
with open() as f
f.write()
f.close()
'''

with open("ficheroenpython2.txt","w") as f:

    f.write("Este es mi primer programa de fichero y lo he escrito en python usando la \nforma recomendada, que es la siguiente: \n with open() as f \n f.write() \n f.close()")

f.close()