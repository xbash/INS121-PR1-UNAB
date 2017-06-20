#COMO LEER
file = open("20_LeerEscribirEnArchivo.txt", "r")
for x in file:
    print (x)
file.close()

#LEER Y METER A LISTA
file = open('20_LeerEscribirEnArchivo.txt', 'r')
lista = []
for x in file:
    lista.append(x)
print(lista)
file.close()

#ESCRIBIR
file = open("20_LeerEscribirEnArchivo.txt", "w")
file.write("This is a test\n")
file.write("And here is another line")
file.close()