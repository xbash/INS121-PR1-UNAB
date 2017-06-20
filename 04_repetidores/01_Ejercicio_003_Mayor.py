def max (n1, n2):
    if n1 < n2:
        print "El mayor es: ",n2
    elif n2 < n1:
        print "El mayor es: ",n1
    else:
        print "Son iguales"
##max(4,4)

print("Ingresar Primer Valor: ")
a = input()
print("Ingresar Segundo Valor: ")
b = input()
max(a,b)
