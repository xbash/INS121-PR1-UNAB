#python 3.4
#Autor: @kokesepulveda
"""
Consideremos un programa que pide un valor y nos dice si es:
si es múltiplo de dos,
si es múltiplo de cuatro (y por tanto, es múltiplo de cuatro)
si es múltiplo de ocho (y por tanto, es múltiplo de cuatro y de dos)
si no es múltiplo de dos
"""

numero = int(input("Dígame un número: "))
if numero % 2 == 0 and numero % 4 != 0 and numero % 8 != 0:
    print(numero, "es múltiplo de dos")
elif numero % 2 == 0 and numero % 4 == 0 and numero % 8 != 0:
    print(numero, "es múltiplo de cuatro y de dos")
elif numero % 2 == 0 and numero % 4 == 0 and numero % 8 == 0:
    print(numero, "es múltiplo de ocho, de cuatro y de dos")
else:
    print(numero, "no es múltiplo de dos")