#python27
#Autor: Jorge Sepulveda S.
#Ejercicio: determinar el numero mayor entre 2 numeros

print "---------------"
num1=int(raw_input("Ingrese un 1er numero entero : "))
num2=int(raw_input("Ingrese un 2do numero entero : "))
print "---------------"
if (num1>num2):
  print "El numero mayor es",num1
elif (num2>num1):
  print "El numero mayor es",num2
else:
  print "Los numeros ingresados son iguales"
