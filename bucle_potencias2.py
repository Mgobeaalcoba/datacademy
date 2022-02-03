"""
El bucle while es conocido como el bucle fundamental en muchos lenguajes. De hecho el bucle for no es mas que
sugar sintax del bucle while en Python. 
"""

def run():
    number = 2
    potencia = 2
    while number ** potencia <= 1000:
        print(number ** potencia)
        potencia += 1

if __name__ == "__main__":
    run()