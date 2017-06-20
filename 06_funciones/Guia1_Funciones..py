"""
    Supongamos que necesitamos escribir un programa que calcule el número combinatorio C(m,n)

        C(m,n), definido como:

                        C(m,n) = m! / (m-n)! * n!


    Donde n! (el factorial de n) es el producto de los números enteros
    desde 1 hasta n:

                  n!= 1*2*3*4·?·(n-1)*n

    Ejemplo: Factorial de 5= 1*2*3*4*5= 120

"""


n=0
m=0
fact=1
print ("n\n\tCalculo de Factorial de  n")
n = int(raw_input("Ingrese numero   :"))
     
fact=1
for i in range(1, n + 1):
    fact *= i

print " \n\t   El factorial de n  es  :", fact

print "_____________________________________________________________________________________________________________"
       
print "\n\n\tCalculo del  número combinatorio sin funciones; hay que hacer lo mismo tres veces  :"

print "\n\n\t C(m,n), definido como: C(m,n) = m! / (m-n)! * n!  "

m = input ("Ingrese   m   :")
n = input ("Ingrese   n   :")

comb=0
a = 0
b = 0
c = 0

       

# factorial de  m!
fact = 1
for i in range(1, m + 1):
    fact = fact * i
a = fact


# factorial de (m - n)!
fact = 1
for i in range(1, m - n + 1):
    fact = fact * i
b = fact

# factorial de n!
fact = 1
for i in range(1, n + 1):
    fact = fact * i
c = fact

comb=   a/(b*c)


print " \n\n\tEl numero combinatorio de m sobre n  es    :", comb


print "____________________________________________________________________________________________________________"
       

print "\n\n\t\t Calculo Aplicando Funciones"


print " Calculo de numero combinatorio para   m =  ",m , "n = ", n
       
# Se define la funcion 
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f



print "\n\n\t C(m,n), definido como: C(m,n) = m! / (m-n)! * n!  "

m = input ("Ingrese   m   :")
n = input ("Ingrese   n   :")

a=factorial (m)
b=factorial (m-n)
c= factorial (n)

comb=   a/(b*c)

print "\n\n\tEl numero combinatorio de M sobre N es   :",comb  
