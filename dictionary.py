def run():
    poblacion_paises = {
        'Argentina' : 45000000,
        'Brasil' : 210000000,
        'Colombia' : 50000000
    }

    print(poblacion_paises['Argentina'])

    for pais in poblacion_paises.keys():
        print(pais)

    for poblacion in poblacion_paises.values():
        print(poblacion)

    for pais, poblacion in poblacion_paises.items():
        print(pais+" : "+str(poblacion))

if __name__ == '__main__':
    run()