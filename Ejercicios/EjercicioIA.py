# EJERCICIO 6.1

'''
6. Escribe un programa en Python que pregunte al usuario por teclado un nombre, primer
apellido, edad y teléfono y lo guarde en un diccionario llamado MiDiccionario. (1 punto)

Para los valores, por ejemplo,

Nombre=Harry, Apellido=Pofer, edad=18 y teléfono=666666666

                       
Tendrá que imprimir por pantalla el mensaje equivalente a:
”Harry Poter Tiene 18 años y su teléfono es 666666666”.



Modifícalo para que:
1- cambie el número (mayor o igual a 1 y menor de 100)correspondiente a la edad a letra. Por ejemplo, si el usuario escribe un 1, 24 ó 33, el programa lo transformaría en:

 1 - "un", quedando la frase final: "Harry Poter tiene un año y su teléfono es...."

 24 -  "veintiun", quedando la frase final: "Harry Poter tiene veintiun años y su teléfono es...."
 33 - "treinta y tres", quedando la frase final: "Harry Poter tiene treinta y tres años y su teléfono es...."

'''


# EJERCICIO CON LISTAS

def convertir_edad(edad):

    unidades = {
        0 : "cero",
        1 : "uno",
        2 : "dos",
        3 : "tres",
        4 : "cuatro",
        5 : "cinco",
        6 : "seis",
        7 : "siete",
        8 : "ocho",
        9 : "nueve"
    }

    decenas = {
        1 : "dieci",
        2 : "veinti",
        3 : "treinta y ",
        4 : "cuarenta y ",
        5 : "cincuenta y ",
        6 : "sesenta y ",
        7 : "setenta y ",
        8 : "ochenta y ",
        9 : "noventa y "
    }

    digitos = [int(a) for a in str(edad)]
    #print(digitos)

    if len(digitos) > 1:

        decena = digitos[0]
        unidad = digitos[1]

        #print('Decena: ' + str(decena))
        #print('Unidad: ' + str(unidad))

        decena_letra = decenas.get(decena)
        unidad_letra = unidades.get(unidad)

        if unidad == 0:

            if decena == 1:
                edad_letra = "diez"
            if decena == 2:
                edad_letra = "veinte"
            if decena == 3:
                edad_letra = "treinta"
            if decena == 4:
                edad_letra = "cuarenta"
            if decena == 5:
                edad_letra = "cincuenta"
            if decena == 6:
                edad_letra = "sesenta"
            if decena == 7:
                edad_letra = "setenta"
            if decena == 8:
                edad_letra = "ochenta"
            if decena == 9:
                edad_letra = "noventa"

        elif decena == 1:
            if unidad == 1:
                edad_letra = "once"
            if unidad == 2:
                edad_letra = "doce"
            if unidad == 3:
                edad_letra = "trece"
            if unidad == 4:
                edad_letra = "catorce"
            if unidad == 5:
                edad_letra = "quince"
            if unidad == 6:
                edad_letra = decena_letra + unidad_letra
            if unidad == 7:
                edad_letra = decena_letra + unidad_letra
            if unidad == 8:
                edad_letra = decena_letra + unidad_letra
            if unidad == 9:
                edad_letra = decena_letra + unidad_letra
        else:
                 edad_letra = decena_letra + unidad_letra

        #print('El numero ' + str(edad) + ' en letras es: ' + edad_letra)
        return edad_letra

    else:
        unidad = digitos[0]
        unidad_letra = unidades.get(unidad)
        #print('Unica unidad: ' + str(unidad))
        #print('El numero ' + str(edad) + ' en letras es: ' + unidad_letra)
        return unidad_letra

def inicio():
    nombre = str(input("Introduzca su nombre: "))
    apellido = str(input("Introduzca su apellido: "))
    edad = int(input("Introduzca su edad: "))
    edad_letra = convertir_edad(edad)
    telefono = int(input("Introduzca su telefono: "))

    print("Me llamo " + nombre + " " + apellido + " tengo " + edad_letra + " anios y mi numero es: " + str(telefono))

# inicio()

# EJERCICIO SIN LISTAS

