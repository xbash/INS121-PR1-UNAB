#Lista de palabras que permite buscar una palabra y eliminarla de la lista
numero = int(input("Dime cuantas palabras tiene la lista: "))

if numero < 1:
    print("Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dime la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es: ", lista)

    eliminar = input("Palabra a eliminar: ")
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == eliminar:
            del(lista[i])
    print("La lista es ahora: ", lista)