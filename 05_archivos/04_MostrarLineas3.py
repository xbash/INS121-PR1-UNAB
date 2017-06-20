#Unidad archivos
#Metodo .readline() lee la siguiente linea en un archivo abierto y lo devuelve como un string

#Se abre el archivo en modo lectura
archivo = open("04_MostrarLineas3.txt","r")
#El contenido de la linea del archivo se pasa a variable string
linea = archivo.readline()

#Se recorre el archivo y se va imprimiendo linea a linea
print("")
while linea:
	print(linea),
	linea = archivo.readline()
archivo.close()
