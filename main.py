from clases.parking import Parking

if __name__ == '__main__':
    niveles_json: str = "resources/niveles.json"

    parking: Parking = Parking(niveles_json)

    nivel: int = 0

    parking.cargar_nivel(nivel)

    while not parking.fin_nivel():
        print(parking)

        mov: str = input("Introduzca movimientos: ")

        for c in mov:
            if not parking.mover_coche(c) and parking.fin_nivel():
                break

        print("\n"*5)

    print(f"Fin nivel {nivel}")

    # parking.cargar_nivel(0)
    #
    # print(parking)

    # print([coords for coords in parking.coches[0]])
    # print(parking.coches[0].letra, chr(ord(parking.coches[0].letra) + 32))
