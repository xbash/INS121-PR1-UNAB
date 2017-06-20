#//////////////////////////////////////////////
#////   UNAB - Facultad Ingenieria         ////
#////   07-05-2016 Santiago, Chile         ////
#////   Autor: Isui Rojas M.               ////
#////   Ing. en Computacion e Informatica  ////
#//////////////////////////////////////////////

# Funcion para calcular la sucesion de fibonacci
# de forma recursiva
def fibonacci_I(n):
	# se declara el caso base para los terminos 1 y 2 que son 1
	if n == 1 or n == 2:
		return 1
	else:
		# Ejemplo: 3
		# (3-1) + (3-2) = 1 + 1 = 2 = 2
		# (4-1) + (4-2) = 3 + 2 = 1 + .2 = 3
		# (5-1) + (5-2) = 4 + 3 = 3 + 1 = 2 + .1 + .2 = 5
		#  etc...
		return fibonacci_I(n-1) + fibonacci_I(n-2)

# Se Verifica la sucesion mostrando en pantalla los valores de cada termino
print fibonacci_I(1)
print fibonacci_I(2)
print fibonacci_I(3)
print fibonacci_I(4)
print fibonacci_I(5)
print fibonacci_I(6)
print fibonacci_I(7)
print fibonacci_I(8)
print fibonacci_I(9)
print fibonacci_I(35)

# Otra manera de hacer la sucesion es la siguiente

def fibonacci_II(n):
	# Recorre fibonacci de la manera tradicional
	# de forma iterativa 
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	# retorna valor esperado
	return a

# Se Verifica la sucesion mostrando en pantalla los valores de cada termino
print fibonacci_II(1)
print fibonacci_II(2)
print fibonacci_II(3)
print fibonacci_II(4)
print fibonacci_II(5)
print fibonacci_II(6)
print fibonacci_II(7)
print fibonacci_II(8)
print fibonacci_II(9)
print fibonacci_II(50)

## Este ejercicio muestra la diferencia de funciones recursiva e iterativa en velocidad
## Se puede apreciar que en la recursiva el termino 35 tarda mucho en calcular
## Y en la iterativa se tiene el termino 50 y lo calcula mucho mas rapido.