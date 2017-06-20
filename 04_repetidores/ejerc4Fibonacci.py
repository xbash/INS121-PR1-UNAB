print '    Serie de Fibonacci '

print '\n\n(1, 1, 2, 3, 5. 8, 13, 21, 34....)'

num = input ('\n Ingrese cantidad de terminos  :')

n1=1
n2=1
n3=0
cont=1
print n1
print n2

while cont<=num:
    n3=n1+n2
    print n3
    n1=n2
    n2=n3
    cont+=1

print 'Fin '

