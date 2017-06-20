#python 3.4
mayor=-9999999999999999999
menor=0
for i in range(1,5):
    valor=int(input("Ingrese el numero: "))
    if valor>mayor:
        mayor=valor
    else:
        menor=valor
print("El numero mayor es ",mayor)
print("El numero menor es ",menor)
