#python27
#programa que muestra la serie de fibonacci
#1,1,2,3,5,8,13,21,43...

num = input ("Ingrese cantidad de terminos a mostrar: ")
n1 = 1
n2 = 1
n3 = 0
cont = 1
numera = cont
print n1
print n2

while cont <= num:
    n3=n1+n2
    print n3
    n1= n2
    n2 = n3
    cont = cont + 1

print "---Fin---"

