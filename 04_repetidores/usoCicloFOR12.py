#python 3.4
#Autor: @kokesepulveda
"""
Uso de contador
"""

print("Comienzo")
cuenta = 0
for i in range(1, 11):
    if i % 3 == 0:
        cuenta = cuenta + 1
print("Desde 1 hasta 10 hay", cuenta, "múltiplos de 3")