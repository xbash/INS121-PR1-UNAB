"""
Ejercicio.- 6. Desarrolle un diagrama de fl
ujo que determine si un triangulo es rectangulo, obtusangulo o acutangulo.
Recuerde que un triangulo es rectangulo si uno de sus angulos es recto 90 grados, es obtusangulo, si uno de sus angulos
es > 90º y acutangulo si todos sus angulos son < 90º, ademas su algoritmo debe pedir nuevamente los angulos
si no son validos para un triangulo.
"""

print "\t\t Determine el tipo de Triangulo segun sus anguulos"

print "\n\t Ingrese tres angulos "

A=0
B=0
C=0
A= int(raw_input("Ingrese angulo A :"))
B= int(raw_input("Ingrese angulo B :"))
C= int(raw_input("Ingrese angulo C :"))

if A+B+C == 180:
    if A==90 or B==90 or C==90:
        print " Es un triangulo Recto"
    elif A >90 or B >90 or C >90:
        print " Es un triangulo Obtusangulo"
    else:
        print " Es un triangulo Acutangulo"

else:
    print "Error, no es un triangulo. La suma de sus angulos no es 180º"
