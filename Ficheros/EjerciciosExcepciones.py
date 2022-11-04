#EJERCICIO 1
'''
Escribe un programa en python que escriba de la forma clasica en un 
fichero llamado "ficheroenpython.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en python usando 
la forma clásica, que es la siguiente:
f = open()
f.write()
f.close()


try:
    f = open("ficheroenpython.txt","w")

    f.write("Este es mi primer programa de fichero y lo he escrito en python usando la forma clasica, que es la siguiente: \n f = open() \n f.write() \n f.close()")

    f.close()

except FileExistsError:

    print("Fichero ya existe")


'''

#EJERCICIO 2

'''
Escribe un programa en python que escriba de la forma clasica en un 
fichero llamado "ficheroenpython2.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en python usando 
la forma recomendada, que es la siguiente:
with open() as f
f.write()
f.close()
'''

try: 
    
    with open("ficheroenpython2.txt","w") as f:

     f.write("Este es mi primer programa de fichero y lo he escrito en python usando la \nforma recomendada, que es la siguiente: \n with open() as f \n f.write() \n f.close()")

    f.close()

except FileExistsError:
    
    print("Fichero ya existe")