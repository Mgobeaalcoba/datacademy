"""
Impresión de 1000 primeros numeros impares
"""
def run():
    numero = 0
    TOPE = 998
    while numero <= TOPE:
        numero += 1 
        if numero % 2 == 0:
            continue
        else:
            print(numero)

if __name__ == "__main__":
    run()