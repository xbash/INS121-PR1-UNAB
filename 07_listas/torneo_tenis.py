#-------------------------------------------------------------------------------
# Nombre:      Torneo de tenis
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
jugadores = []
 
for i in range(1, 9):
    jugador = raw_input("Jugador " + str(i) + ": ")
    jugadores.append(jugador)
 
print
print "Ronda 1"
semifinales = []
 
for i in range(4):
    ganador = raw_input("a." + jugadores[2*i] + " - b." + jugadores[2*i + 1] + ": ")
    if ganador == 'a':
        semifinales.append(jugadores[2*i])
    elif ganador == 'b':
        semifinales.append(jugadores[2*i + 1])
 
print
print "Ronda 2"
finales = []
 
for i in range(2):
    ganador = raw_input("a." + semifinales[2*i] + " - b." + semifinales[2*i + 1] + ": ")
    if ganador == 'a':
        finales.append(semifinales[2*i])
    elif ganador == 'b':
        finales.append(semifinales[2*i + 1])
 
print
print "Ronda 3"
ganador = raw_input("a." + finales[0] + " - b." + finales[1] + ": ")
 
if ganador == 'a':
    print "Campeon:", finales[0]
elif ganador == 'b':
    print "Campeon:", finales[1]