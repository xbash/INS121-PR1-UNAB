#python 3
def bubbleSort(lista):
  for passnum in range(len(lista)-1,0,-1):
    print(lista)
    for i in range(passnum):
      if lista[i] > lista[i+1]:
        temp = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = temp

lista=[20,34,55,12,66,2,99,22,45,87,103,2,14,33,333,2,90]
bubbleSort(lista)
print(lista)
