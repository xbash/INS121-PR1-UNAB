nombres = {}
file = open('teclado.txt', 'r')
for x in file:
    liso = x.partition(" ")
    nombres[liso[0]] = liso[2]
file.close()
for i in range(1,10):
    print('nombre')
    nombre=input()
    print(nombres[nombre])