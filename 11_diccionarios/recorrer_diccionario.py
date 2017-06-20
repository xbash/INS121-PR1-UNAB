#-------------------------------------------------------------------------------
# Name: Recorrido de diccionarios
#
# Author: Carlos Chesta
#-------------------------------------------------------------------------------
 
def hay_valores_pares(d):
	for clave,valor in d.items():
		if valor % 2 == 0:
			return True
		return False
 
def maximo_par(d):
mayor = -float('inf')
for clave,valor in d.items():
if clave + valor &gt; mayor:
mayor = clave + valor
return mayor
 
def invertir(d):
dicc={}
for clave,valor in d.items():
dicc[valor]=clave
return dicc
 
apodos = { 'Suazo': 'Chupete', 'Sanchez': 'Maravilla', 'Medel': 'Pitbull', 'Valdivia': 'Mago',}
 
d1 = {1: 2, 3: 5}
d2 = {2: 1, 6: 7}
d = {5: 1, 4: 7, 9: 0, 2: 2}
 
print invertir(apodos)