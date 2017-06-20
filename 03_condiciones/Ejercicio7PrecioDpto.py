"""Un edifcio tiene 20 pisos de 8 departamentos cada uno. La dueña del edifcio ha defnido una estrategia para
ponerle precio a cada departamento.
El numero que identifica cada departamento se divide en dos partes: los dos ultimos digitos indican en que posicion
esta (de acuerdo al diagrama), y los dos primeros indican el piso. Por ejemplo, el departamento 1105 esta en
el undecimo piso, en la posicion 5.

Los dos departamentos al extremo derecho tienen vista al mar, y los dos al extremo izquierdo tienen vista al
cerro.
Todos los departamentos del primer piso cuestan 100, y todos los departamentos del ultimo piso cuestan 400.

Para los pisos intermedios, se ha dejado un precio base de 250; el precio de los departamentos con vista al
mar se aumentar en un 15 %, y los con vista al cerro se rebajar en un 20 %.

Vista al cerro      0 1 2 3 4 5 6 7     Vista al mar

 (recordar que en una lista llos caracteres se identifican desde la posicion 0  a  n-1)

Desarrolle un diagrama de
ujo que lea el nmero del departamento y entregue como salida el precio del mismo

Ejercicio Basado en PPT Unidad II

"""

#Desarrollo:

numdpto="    "
piso="  "
num="  "
print "\n\n\tCalculo Precio de Departamento"

numdpto= raw_input("Ingrese Numero de Dpto (4 digitos) :")
piso =numdpto[0]+numdpto[1]
if piso=="01":
    print"El Departamento esta en el 1er Piso y vale $100 dolares"
elif piso=="20":
      print"El Departamento esta en el Piso 20 y vale $400 dolares"

num=numdpto[2]+numdpto[3]
if piso!="01" and piso !="20" and num=="01":
    print"Departamento posicion intermedia con vista al cerro, el precio es : base $250 - 20%  --> Precio Final es :", 250*0.80, "dolares"
elif piso!="01" and piso !="20" and num=="08":
    print "Departamento posicion intermedia con vista al mar, su precio es:  base $250 + 15%  -->   Precio Final es :", 250+250*0.15, "dolares"
else:
     print "Departamento posicion intermedia sin vista al cerro, sin vista al mar su precio es:  ", 250, "dolares"
