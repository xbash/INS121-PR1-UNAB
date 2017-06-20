#python 3.4
#Autor: @kokesepulveda
#Ayudante: francisco@banku.cl
#Calcular el valor de PI
#z(SUMATORIA)n=0 (-1)^n/2n+1
zeta = int(input("Ingrese el valor maximo para calcular PI: "))
var = 0
var = float(var)
for n in range(zeta):
    var = var + (((-1)**n)/((2**n)+1))
print(var*4)
