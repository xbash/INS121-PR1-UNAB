#Unidad archivos

from random import uniform

#Se abre o se crea el archivo en modo lectura
archivo = open("03_MostrarNumeros2.txt","w")
print("1.- Abriendo el archivo en modo escritura")

#Se crea un contador hasta 10
contador = 0
#Se escribiran 10 numero al azar en el archivo
print("2.- Escribiendo 10 numeros al azar en el archivo")
while contador < 10:
	numero = round(uniform(1.0,7.0),1)
	valor = str(numero) + '\n'
	archivo.write(valor)
	contador = contador + 1
archivo.close()

#Se abre el archivo en modo lectura
print("3.- Abriendo el archivo en modo lectura e imprimiendo su contenido\n")
archivo = open("03_MostrarNumeros2.txt","r")
contenido = archivo.read()
#Se imprime el contenido del archivo
print(contenido)
print("FIN --------------------")

