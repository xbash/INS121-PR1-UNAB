""" Ejercicio 10.
Desarrolle un diagrama de fujo de un algoritmo que calcule y escriba todas las combinaciones que den por
resultado un numero n natural (6) al sumar 3 numeros naturales distintos.
Ejemplo con n = 10 : 1 + 2 + 7; 1 + 3 + 6; 1 + 4 + 5; 2 + 3 + 5.
"""
# Desarrollo:

print " Para n = 10"
n=10

for i in range(1,n,1):
    for j in range(1,n,1):
        for k in range(1,n,1):
            suma=i+j+k
            #print i, j, k
           
       
            if (i!=j) and (j!=k):
                if suma ==10:
                    print "\n La suma de los numeros :", i, " , ", j, " , ", k
                    print "cumplen con ser :",  suma, "= 10 \n"

print "Fin Programa "
                    
