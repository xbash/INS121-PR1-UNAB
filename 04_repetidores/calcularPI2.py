#python 3.4
#Autor: @kokesepulveda
#Ayudante: francisco@banku.cl
#Calcular el valor de PI

while True:
    zeta=int(input("Ingrese un limite de un rango para calcular PI: "))
    var=0
    var=float(var)
    for n in range(zeta):
        var = var +((-1)**n/((2*n)+1))
    print(var*4)

