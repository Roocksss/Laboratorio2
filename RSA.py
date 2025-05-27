import random

def main():
    try:
        p = int(input("Ingresa un número primo p: "))
        q = int(input("Ingresa otro número primo q: "))
    except ValueError:
        print("Ingresa un número primo válido")
        return

    print("Perfecto")

    n = p * q
    On = (p - 1) * (q - 1)

    e = random.randint(2, On - 1)
    while euclides(e, On) != 1:
        e = random.randint(2, On - 1)

    d = inv_mult(e, On)
    if d is None:
        print("No tiene inverso multiplicativo.")
        return

    llave_publica = (n, e)
    llave_privada = (n, d)

    print("Llave pública: ", llave_publica)
    print("Llave privada: ", llave_privada)

    C = None 

    while True: 
        print ("\n¿Qué deseas hacer?")
        print("1. Cifrar un mensaje")
        print("2. Descifrar un mensaje")
        print("3. Salir") 
        opcion = input("Selecciona una opción (1/2/3): ")
        if opcion == '1':
            M = int(input("Ingresa el mensaje (número entero) a cifrar: "))
            C = cifrar(M, llave_publica)
            print("Mensaje cifrado:", C)
        elif opcion == '2':
            if C is None:
                print("Primero debes cifrar un mensaje.")
                continue
            D = descifrar(C, llave_privada)
            print("Mensaje descifrado:", D)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")
   
def cifrar(M, llave_publica):
    n, e = llave_publica
    return expon_mod(M, e, n)

def descifrar(C, llave_privada):
    n, d = llave_privada
    return expon_mod(C, d, n)

def euclides(a, b):
    if a == 0:
        return b
    else:
        return euclides(b % a, a)

def inv_mult(A, N):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    g, x, y = egcd(A % N, N)
    if g != 1:
        return None
    return (x % N + N) % N  # Positvo 

def expon_mod(a, k, N):
    b = 1
    A = a % N
    if k == 0:
        return b
    if k & 1:      # Bit a bit 
        b = A
    k >>= 1
    while k > 0:
        A = (A * A) % N
        if k & 1:       # Bit a bit
            b = (b * A) % N
        k >>= 1
    return b

main()



