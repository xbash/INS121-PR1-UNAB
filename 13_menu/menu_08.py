class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

n = input("Ingrese numero: ")
while switch(n):
    if case(0):
        print "You typed zero"
        break
    if case(1, 4, 9):
        print "n is a perfect square."
        break
    if case(2):
        print "n is an even number."
    if case(2, 3, 5, 7):
        print "n is a prime number."
        break
    if case(6, 8):
        print "n is an even number."
        break
    print "Only single-digit numbers are allowed."
    break
print "Saliendo..."