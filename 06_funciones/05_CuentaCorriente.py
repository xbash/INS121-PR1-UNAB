## Ejercicio funciones
## El banco "ABC" requiere una aplicacion para control de la CTA.CTE de Clientes.
def menu():
    opc=0
    print("\n\n\tmenu: ")
    print("1. Consulta Cuenta Corriente: ")
    print("2. Giro: ")
    print("3. Deposito: ")
    print("4. Salir ")
    
    opc = input("Ingrese opcion: ")
    return (opc)

def consulta_ctacte(num_cta,rut,nombre,saldo):
    print("\n\nEl estado de tu Cuenta Corriente es: ")
    print("Numero de Cuenta: ", num_cta)
    print("Rut: ", rut)
    print("Nombre: ", nombre)
    print("Saldo: ", saldo)
 
    
def giro(saldo):
    montogiro = 0
    montogiro = input("ingrese monto giro: ")
    saldo = int(saldo - montogiro)
    return(saldo)


def deposito(saldo):
    monto = 0
    monto = input("Ingrese monto deposito  :")
    saldo = saldo + monto
    return(saldo)


# Variables
num_cta=0
rut = " "
nombre = " "
saldo = 0
opc = 0

print("\t\tCreacion Cuenta Corriente")
num_cta = int(input("ingrese numero de cuenta corriente: "))
rut = int(input("ingrese rut: "))
nombre = input("Ingrese nombre: ")
saldo=input("Ingrese saldo: ")

while opc!=4:
    opc = menu()
    if opc == 1:
        consulta_ctacte(num_cta,rut,nombre,saldo)
    elif opc == 2:
        saldo = giro(saldo)
        print("\n\n El saldo despues del giro es: ",saldo)
       
    elif opc == 3:
        saldo=deposito(saldo)
        print("\n\n El saldo despues del deposito es: ",saldo)
print("Fin del proceso:")
print("El estado de la cuenta corriente es: ", consulta_ctacte(num_cta,rut,nombre,saldo))

            
