#leer y mostrar los datos de un archivo

file = open("17_EscribirArchivo.txt","r")
for x in file:
	print(x)
file.close()