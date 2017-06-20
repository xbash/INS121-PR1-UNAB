#python 3.4
#Autor: @kokesepulveda
#len cuenta el ultimo elemento de la variable
lista=["Leonidas","Hipodromo","Jorge","Helicopteros","Paparamericano"]
maxilen = len(lista[0])
maxpalabra = lista[0]
for i in lista:
    if len(i) > maxilen:
        print (len(i))
        maxpalabra = i
        maxilen = len(i)
print(maxpalabra)
