diccionario = {'a':1,'b':2,'c':3}
print "#diccionario"
print diccionario

print "-"*10
print "#imprime el valor del elemento con llave 'a'"
print diccionario['a']

print "-"*10
print "#imprime las llaves del diccionario"
llaves = diccionario.keys()
for i in llaves:
	print i #imprime las llaves del diccionario

print "-"*10
print "#imprime los valores del diccionario"
valores = diccionario.values()
for i in valores:
	print i

print "-"*10
print "#Devuelve el valor del elemento con clave key, en otro caso devuelve default"
print diccionario.get('a')
print diccionario.get('d') #en caso no existe llave devuelve defaul
print diccionario['c']

print "-"*10
print "#Devuelve una lista de tuplas formadas por los pares llaves:valor"
pares = diccionario.items()
for i in pares:
	print i