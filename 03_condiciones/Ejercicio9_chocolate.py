"""

Charlie visita la fabrica de chocolates para comprar, obviamente, chocolates. Cada chocolate cuesta $100,
Hay una promocion de reciclaje, que consiste en lo siguiente: si se retornan 3 envoltorios de chocolate obtienes
un chocolate gratis. Desarrolle un diagrama de fl
ujo que lea cuanto dinero tiene Charlie inicialmente y calcule
(y escriba) cuantos chocolates puede comer y cuantos envoltorios le sobran.

"""

# Desarrollo

monto=0
print "\t Valor de 1 chocolate : $100. Promocion: Por tres envoltorio 1 mas"
monto =input("Ingrese cantidad de dinero que tiene Charlie para gastar:  ")
cant_choc=int(monto / 100)

adicional= int(cant_choc/3)

if adicional > 0:
    print "Charlie con:  ", monto, "compra :", cant_choc, "adicionalmente  :", adicional
    print "En Total  :", cant_choc + adicional
    print "Vuelto   :", monto - (cant_choc*100)
