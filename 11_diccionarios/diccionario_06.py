
print "operaciones con diccionario"
print "mostrar los elementos de un diccionario por item: clave y valor"
diccionario = {'color':'rojo','numero':'4','talla':'M'}
for clave, valor in diccionario.items():
	print "el valor de la clave %s es %s"%(clave,valor)

print "\nla cantidad de elementos mediante la funcion len"
diccionario2 = {'pais':'chile','club':'huachipato','auto_marca':'nissan'}
print "diccionario original: ",diccionario2
print "y su largo es: ",len(diccionario2) #largo 4

print "obtener las claves y valores de un diccionario"
