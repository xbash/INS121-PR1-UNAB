#sumatoria
# @kokesepulveda
while True:
    limit = int(input("Ingrese el limite? "))
    acum = 0
    for i in range(limit+1):
        acum += i**2
    print(acum)
