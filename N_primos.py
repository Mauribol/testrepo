""" Este programa recibe un número N, tal que  0<N<50 y devuelve los números
    primos menores a N.
    Creado por: Ing. Mauricio Bolaños
    Fecha: 19-04-2022
    Versión: 0.0.1"""

def primalidad(N):
    primos = []
    
    if N < 500:
        for i in range(2, N + 1):
            c = 0
            for j in range(2, i + 1):
                if j == i:
                    continue
                if i % j == 0:
                    c += 1
            if c == 0:
                primos.append(i)
        return primos
    else:
        print("N tiene que ser menor que 50")


def run():
    N = int(input("Escribe un numero N<50: "))
    print(primalidad(N))


if __name__ == "__main__":
    run()


    
            
