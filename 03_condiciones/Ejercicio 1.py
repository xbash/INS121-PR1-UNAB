print "\t\t  Calculo de IMC y Riesgos en la Salud"
peso=0
altura=0
edad=0
imc=0

print "\tIngrese los siguientes datos   :"
peso=input('     Peso   :  ')
altura=input('    Altura:')
edad=input('      Edad  :')

imc=peso/altura**2



if imc < 22 and edad< 45:
    print ("Riesgo Bajo")
elif imc<22 and edad >= 45:
    print "Riesgo Medio"
elif imc >=22 and edad < 45:
    print "Riesgo Medio "
elif imc >= 22 and edad >= 45:
    print "Riesgo Alto "
    
