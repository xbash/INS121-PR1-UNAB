// COMO LEER
file = open('newfile.txt', 'r')
for x in file:
print (x)
file.close()

// LEER Y METER A LISTA
file = open('newfile.txt', 'r')
lista = []
for x in file:
lista.append(x)
print(lista)
file.close()

//ESCRIBIR
file = open("newfile.txt", "w")

file.write("This is a test")

file.write("And here is another line")

file.close()