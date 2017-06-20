#python 3.4
#Autor: @kokesepulveda
"""
Uso de IF ELIF ELSE
"""

edad = int(input("¿Cuántos años tiene? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad >= 0 and edad < 18:
    print("Es usted menor de edad")
elif edad >= 18 and edad < 120:
    print("Es usted mayor de edad")
else:
    print("¿Seguro que tiene", edad, "años?")