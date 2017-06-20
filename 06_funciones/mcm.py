import math
 
""" Funcion para hallar el Maximo Comun Divisor """
def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd
 
""" Funcion para hallar el Minimo Comun Multiplo """
def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm
 
""" Funcion Principal """
# Pedimos los datos al usuario
num1 = int(raw_input("Ingrese el primer numero\n"))
num2 = int(raw_input("Ingrese el segundo numero\n"))
# Mostramos el resultado en pantalla
print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm(num1, num2)))
raw_input()
