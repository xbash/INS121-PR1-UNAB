#python3
#Control laboratorio 3
#Alumno: Jorge Sepulveda S.

#menu principal
print("*********************************************")
print("Bienvenido\n")
print("Productos del dia : ")
print("1) KingFiesta - $1990")
print("2) Cuarto de King - $1590")
print("3) KingPollo - $1890")
print("4) Papas: S, M y XL - $900, $1200, $1700")
print("5) Bebida: S, M y XL - $590, $780, $ 1000")
print("*********************************************")
print("\nIngresa el dia de hoy: ")
print("Lunes (1), Marte(2), Miercoles(3), ")
print("Jueves(4), Viernes(5), Sabado(6), Domingo(7) ")
dia = int(input(">>: "))
resp = int(input("¿El cliente es KingAmigo? s(1)/n(2): "))
while((resp !=1) and (resp!=2)):
  resp = int(input("¿El cliente es KingAmigo? s(1)/n(2): "))
