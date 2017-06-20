def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida = invertida + cadena[indice]
        indice = indice + (-1)
        cont = cont - 1
    return invertida

print("Vamos a intentar de invertir un string")
palabra = input("Ingresa la palabra a invertir: ")
print("La palabra invertida es: ",inversa(palabra))