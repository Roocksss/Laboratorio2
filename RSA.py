#Importar liberías 
import numpy as np 
import random 

def main(): 
    try:
        p = int(input("Ingresa un número primo p: "))
        q = int(input("Ingresa otro númrero primo q: "))
    
    except ValueError: 
        print("Ingresa un número primo válido")
    
    else: 
        print("Perfecto")

        n = p*q
        On = (p-1)*(q-1)
        e = random.randint(2,On-1)
        while euclides(e,On) != 1:
            e = random.randint(2,On-1)
        d = pow(e, -1,On)
        #Generación de la llaves 
        #Llave pública
        llave_publica = (n,e)
        #Llave privada 
        llave_privada = (n,d)
        print("Llave pública: ", llave_publica)
        print("Llave privada: ", llave_privada)

        print("¿Deseas cifrar o descifrar un mensaje? (1/2)")
        opcion = input()
        if opcion == '1':
            M = int(input("Ingresa el mensaje (número entero) a cifrar: "))
            C = cifrar(M, llave_publica)
            print("Mensaje cifrado:", C)
        elif opcion == '2':
            C = int(input("Ingresa el mensaje (número entero) cifrado a descifrar: "))
            D = descifrar(C, llave_privada)
            print("Mensaje descifrado:", D)
        else:
            print("Opción no válida. Por favor, ingresa 1 o 2.")

main() 

def cifrar(M, llave_publica): 
    n, e = llave_publica
    C = pow(M, e, n)
    return C

def descifrar(C,llave_privada):
    n,d = llave_privada
    M = pow(C,d,n)
    return M 

def euclides(a, b): 
    if a == 0: 
        return b
    else: 
        return euclides(b % a, a)

def inv_mult(A,N):

    def egcd(a,b): 
        if a == 0: 
            return b,0,1
        
        g,x1,y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1 

        return g,x,y
    
    g,x,y = egcd(A % N, N)

    if g != 1: 
        return None 

    return (x % N + N) % N  #Positivo

def expon_mod(a,k,N): 
    b=1 
    if k == 0:
        return b

    A = a % N

    if k & 1:   #Bit a bit 
        b = A % N 

    K = k >> 1

    while K > 0:
        A = (A * A) % N
        if K & 1:  #Bit a bit
            b = (b * A) % N
        
        K >>= 1
    
    return b


