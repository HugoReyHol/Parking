from clases.parking import Parking


if __name__ == '__main__':
    niveles_json: str = "resources/niveles.json"

    parking: Parking = Parking(niveles_json)
    parking.cargar_nivel(0)

    print(parking)

    # posiciones = iter(parking.coches[1])
    #
    # print(next(posiciones))
    # print(next(posiciones))
    # print(next(posiciones))
    #
    # print([coords for coords in parking.coches[0]])
    # print(parking.coches[0].letra, chr(ord(parking.coches[0].letra) + 32))