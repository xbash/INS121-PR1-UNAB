"""
11. El jerigonzo es una variante ludica del habla en las que se intercalan slabas entre medio de una palabra en
forma reiterada. Para traducir una oracion a jerigonzo despues de cada vocal se debe agregar el sonido \p" y
luego repetir la vocal. Por ejemplo si tenemos la oracion hola mundo, entonces traducido al jerigonzo sera
hopolapa mupundopo. Desarrolle un diagrama de ujo que traduzca alguna oracion a jerigonzo.
"""
# Desarrollo  Jerigonzo:

cadena=""
largo=0
i=0
aux = " "
cadena= raw_input("\n\tIngrese cadena (solo minisculas) :")
print "\tCadena ingresada  :", cadena
largo=len(cadena)
print "\n\t  Largo de la Cadena  :", largo

while i<=largo-1:
    if (cadena[i]!="a" and  cadena[i]!="e") and  (cadena[i]!="i" and  cadena[i]!="o") and  cadena[i]!="u":
        aux = aux + cadena[i]
    elif  cadena[i] =="a":
        aux =aux + "apa"
    elif  cadena[i] =="e":
        aux =aux + "epe"
    elif  cadena[i] =="i":
        aux =aux + "ipi"
    elif  cadena[i] =="o":
        aux =aux + "opo"
    else:
        aux =aux + "upu"
    i=i+1

print "\n\t  Cadena nueva: ", aux
        
        
    
    
