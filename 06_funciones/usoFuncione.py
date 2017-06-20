#python 3.4
#Autor: @kokesepulveda
#Invierte texto
def fibo(n):
    num1,num2 = 0,1
    while num1<n:
        print(num1, end=" ")
        num1,num2 = num2, num1+num2
    print()

fibo(2000)
