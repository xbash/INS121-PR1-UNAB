lista = ["pato","paralelepipedo","hipototamo","constantinopla","cosa"]
maxilen = len(lista[0])
maxpalabra = lista[0]
for i in lista:
    if len(i) > maxilen:
        #print (len(i))
        maxpalabra = i 
        maxilen = len(i)
print (maxpalabra)
