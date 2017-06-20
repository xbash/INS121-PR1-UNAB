dic = {}
file = open("18_LeerArchivoGrabarEnDiccionario.txt","r")
for x in file:
	palabra = x.partition(" ")
	dic[palabra[0]] = palabra[2]
file.close()

for x in range(1,5):
	nombre = input("Ingresa un nombre en el diccionario: ")
	print(dic[nombre])