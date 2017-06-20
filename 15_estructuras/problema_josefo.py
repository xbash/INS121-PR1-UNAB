#-------------------------------------------------------------------------------
# Name:        Problema de Josefo
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
# Cuando un indice tiene valor 1 es porque esta vivo,
# y cuando tiene 0 es porque esta muerto
def sobreviviente(m, n):
    personas = [1] * m
    i = 1
    while personas.count(1) > 1:
        for j in range(m):
            if i == n and personas[j] == 1:
                personas[j] = 0
                i = 1
            if personas[j] == 0:
                continue
            i += 1
 
    return personas.index(1) + 1
 
print(sobreviviente(12,3))