'''
Implementación del algoritmo de Diffie-Hellman para el intercambio de claves
'''

def main():
    try:
        P = int(input("Ingrese un número primo P: "))
        A = int(input("Ingrese un número A: "))
        B = int(input("Ingrese un número B: "))

    except ValueError:
        print("Por favor, ingrese un número(s) válidos.")

    else:
        G = generar_primitivo(P)
        print(f"El generador primitivo G para P={P} es: {G}")
        print(G)
        print()
        K_A = calcular_clave_publica(A, P, G)
        print(f"La clave pública de Alice es: {K_A}")
        print()
        K_B = calcular_clave_publica(B, P, G)
        print(f"La clave pública de Bob es: {B}")
        print()

        S_A = calcular_secreto(K_B, A, P)
        print(f"El secreto compartido de Alice es: {S_A}")
        print()
        S_B = calcular_secreto(K_A, B, P)
        print(f"El secreto compartido de Bob es: {S_B}")
        print()
    
        


def generar_primitivo(P):
    for i in range(2, P):
        resultados = []
        for j in range(0, P - 2):
            r = pow(i, j, P)
            resultados.append(r)
        if len(resultados) != len(set(resultados)):
            break
    return i

def calcular_clave_publica(x, P, G):
    return pow(G, x, P)

def calcular_secreto(clave_publica, x, P):
    return pow(clave_publica, x, P)


main()