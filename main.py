import json
import time
from clases.parking import Parking


if __name__ == '__main__':
    niveles_json: str = "resources/niveles.json"

    # Crea el objeto Parking para gestionar la partida
    parking: Parking = Parking(niveles_json)

    niveles: int

    # Calcula cuantos niveles existen
    with open(niveles_json, "r") as json_f:
        json_data: dict = json.load(json_f)
        niveles = len(json_data.keys())

    print("Introduce la letra del coche para moverlo, mayuscula adelante, minuscula atras, puedes introducir varias seguidas")

    # Recorre todos los niveles
    for nivel in range(niveles):
        numMov: int = 0 # Almacena los movimientos realizados para acabar el nivel

        # Carga el nivel actual en el objeto Parking
        parking.cargar_nivel(nivel)

        # Este bucle se ejecuta mientras el nivel no haya acabado
        while not parking.fin_nivel():
            # Muestra el estado actual del Parking
            print(parking)

            # Pregunta al usuario la lista de movimientos
            mov: str = input("Introduzca movimientos: ")

            # Realiza este bucle por cada movimiento en el string de movimientos
            for c in mov:
                # Realiza el movimiento c, si es imposible o el nivel ha acabado sale del bucle
                if not parking.mover_coche(c) or parking.fin_nivel():
                    break

                numMov += 1

            print()

        # Al acabar el nivel muestra el estado final del Parking y las estadisticas del nivel
        print(parking)
        print(f"Fin del nivel {nivel + 1} con {numMov} movimientos")

        # Detiene la ejecución del programa 2,5 segundos para que el usuario pueda leer la información anterior
        time.sleep(2.5)
