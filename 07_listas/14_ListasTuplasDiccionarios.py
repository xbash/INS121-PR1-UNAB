
#Se declara lista
a = [1,2,3,4,5,6,7,8]
#imprimir lista completa
print(a)
#imprimir posicion 0
print(a[0])
#imprimir longitud de la lista
print(len(a))
#recorrer e imprimr la lista
for x in range(0,len(a)):
	print (a[x])
	pass
#segunda opcion para recorrer e imprimir la lista
for x in a:
	print(x)
	pass
#insertar elemento al final de la lista
a.append(9)
print(a)
#insertar en una posicion x valor y
a.insert(0,0)
print(a)
#indice del valor x
print(a.index(3))
#true si esta, false lo contrario
print (40 in a)
#determina el mayor de una lista
print(max(a))

#tupla
#declaracion
t=(25, "Mayo", 1810)
#imprimir elementos
print(t[0])
#hacer una tupla con variables
a=125
b="\#"
c="Ana"
d=a,b,c
print (d)
#longitud
print(len(t))
#tupla unitaria
u=(1810,)
print (u)
#tupla anidada
h =(15,(12,21))
print (h[1][1])

#diccionario
materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miÃ©rcoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]
for dia in materias:
	print(dia, ":", materias[dia])
for dia, codigos in materias.items():
	print(dia, ":", codigos)

