#Unidad Archivos

#Abro el archivo en modo lectura
archivo = open("09_MostrarNumeros.txt","r")
#Declaro una lista vacia
lista=[]
#Recorro linea por linea del archivo
for linea in archivo:
	#Tomo cada valor de la linea y lo convierto a real
	valor = float(linea)
	#Agrego cada valor real a la lista vacia
	lista.append(valor) 
	#Cierro el archivo
archivo.close()

#Recorro toda la lista y la imprimo
for i in lista:
	print(i)