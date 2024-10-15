from clases.parking import Parking

if __name__ == '__main__':
    niveles_json: str = "resources/niveles.json"

    parking: Parking = Parking(niveles_json)

    nivel: int = 1
    numMov: int = 0

    parking.cargar_nivel(nivel)

    while not parking.fin_nivel():
        print(
            "Introduce la letra del coche para moverlo, mayuscula adelante, minuscula atras, puedes introducir varias")
        print(parking)

        mov: str = input("Introduzca movimientos: ")

        for c in mov:
            if not parking.mover_coche(c) and parking.fin_nivel():
                break

            numMov += 1

        print()

    print(parking)
    print(f"Fin del nivel {nivel+1} con {numMov} movimientos")
