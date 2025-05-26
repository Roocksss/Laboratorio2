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
        while np.gcd(e,On) != 1:
            e = random.randint(2,On-1)
        d = pow(e, -1,On)
        #Generación de la llaves 
        #Llave pública
        llave_publica = (n,e)
        #Llave privada 
        llave_privada = (n,d)
        print("Llave pública: ", llave_publica)
        print("Llave privada: ", llave_privada)

def cifrar(M, llave_publica): 
    n, e = llave_publica
    C = pow(M, e, n)
    return C

def descifrar(C,llave_privada):
    n,d = llave_privada
    M = pow(C,d,n)
    return M 

main() 

