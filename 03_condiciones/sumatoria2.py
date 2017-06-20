n = int(input("Ingrese el numero para n: "))
m = int(input("Ingrese el numero para m: "))
suma = 0
if n > m:
    print("n debe ser mayor que m")
else:
    for x in range(n,m+1):
        suma += x
    print(suma)
