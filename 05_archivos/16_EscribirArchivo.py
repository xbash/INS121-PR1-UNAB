#ingresar datos por pantalla y grabarlo en archivo

file = open("16_EscribirArchivo.txt","w")
print("Escribir 5 datos:	")
for x in range(1,5):
	letra = input()
	file.write(letra+'\n')
file.close()