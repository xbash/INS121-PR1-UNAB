#python 3.4
#Dada una lista de numeros indicar el numero mayor
Lista=[8,9,-3,4,6,0,-12]
mayor=Lista[0]
for i in Lista:
    if i > mayor:
        mayor=i    
print(mayor)
