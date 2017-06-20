# Codigo de Python 3
def imprime_rango_carta(n):
	def caso_as():
		print('As')
	def caso_num():
		print(n)
	def caso_jota():
		print('Jota')
	def caso_reina():
		print('Reina')
	def caso_rey():
		print('Rey')
	def caso_invalido():
		print('Invalido')
	tabla = { 1: caso_as,   2: caso_num,   3: caso_num,
              4: caso_num,  5: caso_num,   6: caso_num,
              7: caso_num,  8: caso_num,   9: caso_num,
             10: caso_num, 11: caso_jota, 12: caso_reina,
             13: caso_rey }
	
	f = tabla.get(n, caso_invalido)
	f()