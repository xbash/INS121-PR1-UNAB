

def maximo(datos):
    maximo = 0
    for i in datos:
        if i > maximo:
            maximo = i
    return maximo
def minimo(datos):
    minimo = 999999
    for i in datos:
        if i < minimo:
            minimo = i
    return minimo
def promedio(datos):
    suma = 0
    for i in datos:
        suma+=i
    return (suma/len(datos))
#datos = [6,7,7,7,6,6,7]
def moda(datos):
    repeticiones = 0
    for i in datos:
        apariciones = datos.count(i)
        if apariciones>repeticiones:
            repeticiones = apariciones
    modas = []
    for i in datos:
        apariciones = datos.count(i)
        if apariciones == repeticiones and i not in modas:
            modas.append(i)
    return modas

def DobleDe(n):
    return (2*n)

lista = [7,3,4.5,6.2,5.5,5,3,5,4,1.7,6.5,7,7,7]
print("Lista original: ",lista)
print("El maximo es: ",maximo(lista))
print("El minimo es: ",minimo(lista))
print("El promedio es: ",promedio(lista))
print("La moda es: ",moda(lista))
print("El doble de",lista[0],"es: ",DobleDe(lista[0]))
