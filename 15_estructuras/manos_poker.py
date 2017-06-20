#-------------------------------------------------------------------------------
# Nombre:      Manos de poker
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
def es_full(mano):
    conjunto_valor = set()
 
    for i in mano:
        valor, palo = i
        conjunto_valor.add(valor)       # Se agrega al conjunto el valor de la carta
 
    return len(conjunto_valor) == 2     # Si tiene 2 elementos es Full
 
def es_color(mano):
    conjunto_palo = set()
 
    for carta in mano:
        valor, palo = carta
        conjunto_palo.add(palo)
 
    return len(conjunto_palo) == 1
 
def es_escalera(mano):
    lista = []
 
    for carta in mano:
        valor, palo = carta
        lista.append(valor)
 
    lista_ordenada = sorted(lista)
 
    # Recorremos la lista y restamos los elementos adyacentes para ver si es -1
    for i in range(len(lista_ordenada)):
        # Si la iteracion alcanza el ultimo elemento es porque es escalera
        if i == len(lista_ordenada) - 1:
            return True
 
        diferencia = abs(lista_ordenada[i] - lista_ordenada[i + 1])
 
        # Si la diferencia entre dos numeros adyacentes es mayor que 1 no es escalera
        if diferencia > 1:
            return False
 
def es_escalera_de_color(mano):
    conjunto_palo = set()
 
    for carta in mano:
        valor, palo = carta
        conjunto_palo.add(palo)
 
    return es_escalera(mano) and len(conjunto_palo) == 1
 
def es_escalera_real_de_color(mano):
    conjunto_palo = set()
 
    for carta in mano:
        valor, palo = carta
        # Si es As, J, Q o K se agrega el palo al conjunto
        if valor == 1 or valor >= 10:
            conjunto_palo.add(palo)
        else:
            return False
 
    # Si son del mismo color solo habra un elemento en el conjunto
    return len(conjunto_palo) == 1
 
def es_poker(mano):
    contador_cartas = {}
 
    for carta in mano:
        valor, _ = carta
 
        if valor not in contador_cartas:
            contador_cartas[valor] = 1
        else:
            contador_cartas[valor] += 1
 
    for cantidad in contador_cartas.values():
        if cantidad == 4:
            return True
 
    return False
 
def es_trio(mano):
    contador_cartas = {}
 
    for carta in mano:
        valor, _ = carta
 
        if valor not in contador_cartas:
            contador_cartas[valor] = 1
        else:
            contador_cartas[valor] += 1
 
    for cantidad in contador_cartas.values():
        if cantidad == 3:
            return True
 
    return False
 
def es_dobre_pareja(mano):
    conjunto = set()
 
    for carta in mano:
        valor, _ = carta
        conjunto.add(valor)
 
    # Si hay 3 elementos es porque al menos hay un trio o doble par en la mano
    # entonces descartamos que sea trio agregando la condicion que no sea trio
    return len(conjunto) == 3 and not es_trio(mano)
 
def es_pareja(mano):
    conjunto_valor = set()
 
    for carta in mano:
        valor, palo = carta
        conjunto_valor.add(valor)
 
    return len(conjunto_valor) == 4
 
mano = set()
cartas_reales = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
 
for i in range(1, 6):
    carta = raw_input("Carta " + str(i) + ": ")
 
    if carta[0] in cartas_reales:
        valor = cartas_reales[carta[0]]
    else:
        valor = int(carta[:-1])
 
    pica = carta[-1]
    tupla_carta =(valor, pica)
    mano.add(tupla_carta)
 
if es_escalera_real_de_color(mano):
    print "Escalera real"
elif es_escalera_de_color(mano):
    print "Escalera de color"
elif es_poker(mano):
    print "Poker"
elif es_full(mano):
    print "Full"
elif es_color(mano):
    print "Color"
elif es_escalera(mano):
    print "Escalera"
elif es_trio(mano):
    print "Trio"
elif es_dobre_pareja(mano):
    print "Doble pareja"
elif es_pareja(mano):
    print "Pareja"
else:
    print "No forma ninguna combinacion"