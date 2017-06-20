print '\t Un numero N con 4 digitos es un numero doble-cuadrado cuando este'
print '\t igual a la suma de dos numeros alcuadrado: uno formado por los dos'
print '\t primeros digitos de N y el otro formado por los dos ultimos dgitos de N.'
print '\n\nPor ejemplo, 1233 es un numero doble-cuadrado ya que 1233 = 12**2 + 33**2.'

i = 0
j = 0
t1 = 0
t2 = 0
for i in range (10, 100,1):
    #print i**2
    for j in range(10, 100, 1):
        t1= i**2 + j**2
        #print t1
        t2=i*100+j
        #print t2
        if t1==t2:
            print "\n\tPara el numero :", t1, "se cumple que el cuadrado de :", i, "+", "cuadrado de :", j, "es  :", i**2, "+", j**2  
            print "\t Se cumple la suma de los cuadrados ",i**2, "+", j**2, "=" , t1
          

