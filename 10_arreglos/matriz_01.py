
matriz = [
		[4,15,14,1],
		[9,6,7,12],
		[5,10,11,8],
		[16,3,2,13]
]
# arreglo para guardar las sumas y poder verificarlas luego
sumas = []
#tamano de matriz
DIMEN = len(matriz[0])

#Matriz original
print "Matriz Original: ",matriz

#suma filas y guarda datos en arreglo
for i in range(DIMEN):
	suma = 0
	for j in range(DIMEN):
		suma = suma + matriz[i][j]
	sumas.append(suma)

#suma columnas y guarda dato en arreglo
for j in range(DIMEN):
	suma = 0
	for i in range(DIMEN):
		suma = suma + matriz[i][j]
	sumas.append(suma)

#suma diagonal arriba -> abajo
suma = 0
for k in range(DIMEN):
	suma = suma + matriz[k][k]
sumas.append(suma)

#suma diagonal abajo -> arriba
suma = 0
for j in range(DIMEN):
	i = DIMEN - 1 - k
	suma = suma + matriz[i][j]
sumas.append(suma)

ultimaSuma = sumas[0]
for suma in sumas:
	if ultimaSuma != suma:
		print "No es cuadrado magico"
	ultimaSuma = suma
print "Es cuadrado magico"