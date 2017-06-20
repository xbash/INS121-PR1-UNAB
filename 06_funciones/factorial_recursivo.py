#//////////////////////////////////////////////
#////   UNAB - Facultad Ingenieria         ////
#////   30-04-2016 Santiago, Chile         ////
#////   Autor: Isui Rojas M.               ////
#////   Ing. en Computacion e Informatica  ////
#//////////////////////////////////////////////

# Esta es una funcion recursiva la cual consiste en que se llama asi misma
# realizando procesos hasta que llegue a su caso base
# Los casos base son las condiciones que estan en el if
# si no se cumplen las condiciones la funcion retorna un valor realizando un calculo previo
# ademas es un tipo de funcion muy practica en casos particulares


# Defino la funcion mandando un parametro (factorial que deseo calcular)
def factorial(n):
	# Preparo caso base PD: tambien funciona si le sacas el n == 1
	# lo deje asi por caso practico en matematicas
	if n == 0 or n == 1:
		# retorna valor base o resultado calculado
		return 1
	else:
		# paso 1
		# 5 no es base si que (5 * factorial(5-1) )<---- Ese valor queda en el pasado
		# paso 2
		# 4 no es base si que (4 * factorial(4-1) )<---- Ese valor queda en el pasado
		# paso 3
		# 3 no es base si que (3 * factorial(3-1) )<---- Ese valor queda en el pasado
		# paso 4
		# 2 no es base si que (2 * factorial(2-1) )<---- Ese valor queda en el pasado
		# paso 5
		# 1 base si <---- Ese valor queda en el pasado

		## despues magica y misteriosamente
		## la funcion vuelve al pasado toma los valores y multiplica
		## 1 * 2 = 2
		## 2 * 3 = 6
		## 6 * 4 = 24
		## 24 * 5 = 120
		return n * factorial(n - 1)


## el print es para mostrar en pantalla el calculo realizado por la funcion
numero = input("Ingresa el numero: ")
print factorial(numero)
#print factorial(5)
