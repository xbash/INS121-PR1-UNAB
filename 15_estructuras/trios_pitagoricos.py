#-------------------------------------------------------------------------------
# Name:        Trios pitagoricos
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def son_pitagoricos(a,b,c):
    if c == (a**2 + b**2)**0.5:
        return True
    else:
        return False
 
def pitagoricos (n):
    lista = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if son_pitagoricos(i,j,k):
                    lista.append((i,j,k))
 
    return lista