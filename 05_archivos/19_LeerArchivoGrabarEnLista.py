file = open("19_LeerArchivoGrabarEnLista.txt","r")
lista = []
for x in file:
	lista.append(x)
print(lista)
file.close()
