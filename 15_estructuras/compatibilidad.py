#-------------------------------------------------------------------------------
# Name:        Compatibilidad entre personas
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
signos_compatibles = {
#   (mujer, hombre)
    ('aries', 'tauro'),
    ('aries', 'geminis'),
    ('aries', 'cancer'),
    ('aries', 'libra'),
    ('aries', 'escorpion'),
    ('aries', 'sagitario'),
    ('aries', 'acuario'),
 
    ('tauro', 'tauro'),
    ('tauro', 'leo'),
    ('tauro', 'virgo'),
    ('tauro', 'escorpion'),
    ('tauro', 'capricornio'),
    ('tauro', 'piscis'),
 
    ('geminis', 'aries'),
    ('geminis', 'tauro'),
    ('geminis', 'geminis'),
    ('geminis', 'libra'),
    ('geminis', 'acuario'),
    ('geminis', 'piscis'),
 
    ('cancer', 'tauro'),
    ('cancer', 'cancer'),
    ('cancer', 'leo'),
    ('cancer', 'virgo'),
    ('cancer', 'libra'),
    ('cancer', 'escorpion'),
    ('cancer', 'piscis'),
 
    ('leo', 'aries'),
    ('leo', 'tauro'),
    ('leo', 'geminis'),
    ('leo', 'libra'),
    ('leo', 'capricornio'),
 
    ('virgo', 'tauro'),
    ('virgo', 'cancer'),
    ('virgo', 'leo'),
    ('virgo', 'virgo'),
    ('virgo', 'escorpion'),
    ('virgo', 'capricornio'),
    ('virgo', 'acuario'),
    ('virgo', 'piscis'),
 
    ('libra', 'aries'),
    ('libra', 'tauro'),
    ('libra', 'geminis'),
    ('libra', 'cancer'),
    ('libra', 'virgo'),
    ('libra', 'escorpion'),
    ('libra', 'acuario'),
 
    ('escorpion', 'tauro'),
    ('escorpion', 'geminis'),
    ('escorpion', 'cancer'),
    ('escorpion', 'virgo'),
    ('escorpion', 'escorpion'),
    ('escorpion', 'acuario'),
    ('escorpion', 'piscis'),
 
    ('sagitario', 'aries'),
    ('sagitario', 'geminis'),
    ('sagitario', 'leo'),
    ('sagitario', 'virgo'),
    ('sagitario', 'libra'),
    ('sagitario', 'escorpion'),
    ('sagitario', 'sagitario'),
    ('sagitario', 'capricornio'),
    ('sagitario', 'acuario'),
 
    ('capricornio', 'tauro'),
    ('capricornio', 'leo'),
    ('capricornio', 'virgo'),
    ('capricornio', 'capricornio'),
 
    ('acuario', 'aries'),
    ('acuario', 'leo'),
    ('acuario', 'libra'),
    ('acuario', 'sagitario'),
    ('acuario', 'acuario'),
    ('acuario', 'piscis'),
 
    ('piscis', 'aries'),
    ('piscis', 'tauro'),
    ('piscis', 'cancer'),
    ('piscis', 'libra'),
    ('piscis', 'capricornio'),
    ('piscis', 'piscis'),
}
 
def compatibles(p1, p2):
    signos = (p1[4], p2[4])
    if p1[1] != p2[1] and abs(p1[2] - p2[2]) < 10 and p1[3] == p2[3] and signos in signos_compatibles:
        return True
    else:
        return False
 
persona_1 = ('Pepito', 'M', 27, 'rock', 'aries')
persona_2 = ('Yayita', 'F', 23, 'rock', 'tauro')
 
print(compatibles(persona_1, persona_2))