# directorio = dict([tuple(line.split(',')) for line in directorio])

file = "miagendahoy.txt"

#Creo la variable directorio que la convierto en una lista para meter dentro el contenido del fichero
directorio = []
line = str()

f = open(file,'r')
directorio = f.readlines()
print("Compruebo el contenido de directorio:" + directorio + " que es dle tipo " + type(directorio))

#Creo una lista vacia y luego le pasaré el contenido del fichero separado por comas
milista = [] #creo una lisita vacia

# recorro todo el directorio, linea a linea
# a mi lista, le añado (por el final) lo que voy leyendo de directorio y lo separo con comas(split)

for line in directorio:
    print("\n**** El contenido de line es:" + line + " que es del tipo: " + type(milista))

print("\n\n\n\n Por lo que de momento, la lista después de leer el fichero, contiene una lista con tantas listas como pares había en el fichero \n" + milista)
mitupla=tuple(milista)
print("\n\n Convierto la lista de listas en una tupla (fijaros en los parentesis)",mitupla," y comprueblo el tipo de tupla", type(mitupla))

midict = {}

for i in range(len(mitupla)):
    print(mitupla[i]," i=",i)
    midict=dict(mitupla)

print(milista)
print("\n\n El diccionario completo contiene: ", midict)