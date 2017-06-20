nombres = {}
file = open('12_BuscarNombre.txt', 'r')
for x in file:
    palabra = x.partition(" ")
    nombres[palabra[0]] = palabra[2]
file.close()
for i in range(1,10):
    nombre=input("Ingrese un nombre a buscar y se retorna su apellido: ")
    print(nombres[nombre])