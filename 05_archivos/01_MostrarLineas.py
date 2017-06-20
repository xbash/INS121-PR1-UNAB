#python3
#Unidad Archivos

#Abro el archivo en modo lectura
archivo = open("01_lecturaArchivos.txt","r")
#Leo el contenido del archivo y lo vuelvo en una variable
contenido = archivo.read()
#Imprimo el contenido del texto
print(contenido)

archivo.seek(0)
archivo.close()
if archivo.close:
	print("\nEl archivo esta cerrado")
else:
	print("El archivo no esta cerrado")