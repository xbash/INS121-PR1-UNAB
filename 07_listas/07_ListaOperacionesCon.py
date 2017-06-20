#Python3

lista = ['pan','huevos',100,1234]
lista2 = lista[:]
#lista original
print(lista)

#reeemplazar valores
lista[0:2]=[1,2]
print(lista)

#borrar algunos
lista[0:2]=[]
print(lista)

#insertar algunos
lista[1:1]=['lala','asdf']
print(lista)

#insertar una copia de la misma lista al principio
lista[:0]=lista
print(lista)

#vaciar la lista reemplazando todos los items con una lista vacia
lista[:]=[]
print(lista)
print("pan" in lista)

for i in lista2:
	print(i)

#imprime lista al reves
print(lista2[::-1])