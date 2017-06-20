#Ejercicio I: Comparar 2 matrices
mat1 = [[1,2],[4,5],[5,6],[2,6]]
mat2 = [[1,5],[2,4],[8,4],[6,6]]

#Recorrer las 2 matrices y oomparar si los valores son iguales
print "-"*30
print "Matriz 1 : ",mat1
print "Matriz 2 : ",mat2

print "-"*30
for i in range(0,2):
	for j in range(0,2):
		if mat1[i][j] == mat2[i][j]:
			print"En los subindices [%d][%d] son iguales"%(i,j)

#Ejercicio II: Ingresar un numero y ver si se encuentra en las matrices
print "-"*30
num = int(raw_input("Ingresar un numero: "))
for i in range(0,2):
	for j in range(0,2):
		if (mat1[i][j] == num) or (mat2[i][j] == num):
			print"El numero se encuentra en los subindices [%d][%d]"%(i,j)
		else:
			print"El numero no existe en los subindices!"