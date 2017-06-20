#-------------------------------------------------------------------------------
# Nombre:      Sudoku
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
 
def solucion_es_correcta(sudoku):
    # Primero el rango de 1 a 9 para que busque el i en cada combinacion posible
    for i in range(1,10):
        # Los dos siguientes for son para recrear los 9 subcuadrados del sudoku
        for fil in range(3):
            for col in range(3):
                # Los indices para seleccionar un subcuadrado
                mov = range(0,10,3)     # -> [0, 3, 6, 9]
                subcuadrado = sudoku[mov[fil]:mov[fil+1], mov[col]:mov[col+1]]
 
                if i not in subcuadrado or i not in sudoku[:,i-1] or i not in sudoku[i-1,:]:
                    return False
    return True