numero=int(input("Ingrese un numero a evaluar"))
centena=numero/100
decena=(numero&100)/10
unidad=(numero%100)%10
if (centena==unidad):
    print("El numero es capicua")
else:
    print("El numero no es capicua")
