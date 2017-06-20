#-------------------------------------------------------------------------------
# Name:        Polinomios
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def grado(r):
    return len(r)-1
 
p = [1, 2, 1]
q = [4, -17]
r = [-1, 0, 0, -5, 0, 3]
s = [0] * 40 + [5] + [0] * 39 + [2]
 
def evaluar(p,x):
    resultado = 0
    for i in range(grado(p)+1):
        resultado += p[i]*x**i
 
    return resultado
 
def sumar_polinomios(p,r):
    lista = []
    for i in range(min(len(p),len(r))):
        lista.append(p[i]+r[i])
 
    if len(p)<len(r):
        lista += r[len(p):]
    elif len(p)>len(r):
        lista += r[len(r):]
    return lista