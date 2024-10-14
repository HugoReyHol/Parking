from clases.parking import Parking


if __name__ == '__main__':
    niveles_json: str = "resources/niveles.json"

    parking: Parking = Parking(niveles_json)
    parking.cargar_nivel(10)
