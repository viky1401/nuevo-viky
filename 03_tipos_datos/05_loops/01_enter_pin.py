#victoria repol
#07-04-2025


print("Banco del 4°B")

pin = int(input("Ingrese su pin: "))

while pin != 1234:
    print("Pin incorrecto")
    pin = int(input("Ingrese su pin: "))

if pin == 1234:
    print("Pin correcto")
    print("Bienvenido al banco del 4°B")