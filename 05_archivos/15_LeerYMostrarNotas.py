#Leer y escribir a archivo

def escribir():
	# Se abre o se crea el archivo en modo de escritura
    file = open("15_LeerYMostrarNotas.txt","w")
    i = 0
    nota=0.0
    while i < 10:
		#clon = i +1
		#print(clon)
		nota= float(input("Ingrese Nota [Ejem: 3.5]: "))
		valor = str(nota)+"\n"
		file.write(valor)
		i = i + 1
	file.close( )

def leer_Archivo( ):
    # Se abre el archivo en modo de lectura
    file=open("15_LeerYMostrarNotas.txt","r")
    lista = [ ] 
    for linea in file:
        valor = float(linea)
        lista.append(valor)  # agregando nota
    file.close( )
    return lista

# BLOQUE PRINCIPAL
escribir()
print("\nNotas almacenadas")

lista=leer_Archivo()
for i in  lista:
    print(i)
