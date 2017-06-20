"""
En las competencias de clavados, cada salto es evaluado por un panel de siete jueces. Cada juez entrega una
puntuacion en una escala de 1 a 10, con incrementos de 0:5 . La puntuacion mas alta y la mas baja son
eliminadas. La suma de los cinco puntajes restantes es multiplicada por 0.6 , y el resultado es multiplicado
por el grado de difcultad del salto. El valor obtenido es el puntaje total del salto.

Desarrolle un diagrama de flujo que lea el grado de difcultad del salto y los 7 puntajes de los jueces,
para luego mostrar por pantalla el puntaje total del salto.

A continuacion se muestra un ejemplo:
    Grado de dificultad: 3.0
        Juez 1: 5.0
        Juez 2: 5.5
        Juez 3: 4.0
        Juez 4: 5.0
        Juez 5: 4.5
        Juez 6: 5.5
        Juez 7: 5.0
    El puntaje total es 45.0
"""

#  Variables
ptje=0.0
menor=0.0
mayor=0.0
ptjetotal=0.0
gradodif=0
i=1

print "\t\tCalificacion de Saltos Clavados"
print "Ingrese Grado de Dificultad del Salto"
gradodif=input(" Grado  :")
print "Ingrese 7 calificaciones"
ptje=float(raw_input("Calificacion  :"))
menor=ptje
mayor=ptje
ptjetotal =ptjetotal+ptje
for i in range(2,8,1):
    ptje=float(raw_input("Calificacion  :"))
    if menor>ptje:
        menor=ptje
    if mayor<ptje:
        mayor=ptje
    ptjetotal =ptjetotal+ptje
# fuera del ciclo    
ptjetotal=ptjetotal-(mayor+menor)
ptjetotal=ptjetotal*0.6
ptjetotal=ptjetotal*gradodif
print"\n\n\t\t  Puntaje Total del Salto  :", ptjetotal

        
"""
Resultado ejecucion:

		Calificacion de Saltos Clavados
Ingrese Grado de Dificultad del Salto
 Grado  :3
Ingrese 7 calificaciones
Calificacion  :5
Calificacion  :5.5
Calificacion  :4
Calificacion  :5
Calificacion  :4.5
Calificacion  :5.5
Calificacion  :5


		  Puntaje Total del Salto  : 45.0

"""
