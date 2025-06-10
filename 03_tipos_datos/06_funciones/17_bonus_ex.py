#victoria repol

#Repetir hasta que lo hagan bien podemos usar bucles junto pcn un try 

def pedir_numero_repetido():
    while True:
        try:
            num = int(input("Escribe un numero entero:"))
            print(f"!Gracias tu numero es:{num}")
            break
        except ValueError:
            print("Esa no es una respuesta valida")

pedir_numero_repetido()


