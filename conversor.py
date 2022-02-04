def conversor(cantidad, tipocambio):
    return cantidad / tipocambio

def run():
    print(
    """
    Bienvenido al conversor de criptocriptos a dolares:

    Seleccione la criptocripto a la que desea convertir sus dolares a traves de su numero de identificación: 

    1- Bitcoin
    2- Ether
    3- Cardano
    4- Algorand
    5- Polkadot
    
    """)
    cripto = int(input())
    while cripto < 1 or cripto > 5:
        cripto = int(input("Ingreso un valor inexistente. Por favor seleccione nuevamente su cripto: "))

    dolares = float(input("Ingrese la cantidad de dolares que desea convertir a cripto: "))
    bitcoin = 37443.63
    ether = 2484.83
    cardano = 1.06
    algorand = 0.91
    polkadot = 18.96

    if cripto == 1:
        resultado = str(conversor(dolares, bitcoin))
        print("Usted tiene el equivalente a: "+resultado+" bitcoins.")
    elif cripto == 2:
        resultado = str(conversor(dolares, ether))
        print("Usted tiene el equivalente a: "+resultado+" ethers.")
    elif cripto == 3:
        resultado = str(conversor(dolares, cardano))
        print("Usted tiene el equivalente a: "+resultado+" cardanos.")
    elif cripto == 4:
        resultado = str(conversor(dolares, algorand))
        print("Usted tiene el equivalente a: "+resultado+" algorands.")
    else:
        resultado = str(conversor(dolares, polkadot))
        print("Usted tiene el equivalente a: "+resultado+" polkadots.")

if __name__ == "__main__":
    run()