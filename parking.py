from coche import Coche
import json


class Parking:
    coches: list[Coche] = []
    salida: tuple[int, int] = ()
    filas: int = 0
    columnas: int = 0
    nivel: int = 0

    def __init__(self, niveles_json: str):
        self.niveles_json = niveles_json

    # Carga el nivel actual en la lista de coches
    def cargar_nivel(self, nivel: int) -> bool:
        try:
            with open(self.niveles_json, "r") as json_f:
                json_data: dict = json.load(json_f)

                if len(json_data.keys()) < nivel:
                    print("No existe ese nivel")
                    return False

                nivel_data: dict = json_data[f"{nivel}"]
                self.filas = nivel_data["filas"]
                self.columnas = nivel_data["columnas"]
                self.salida = tuple(nivel_data["salida"])
                self.coches = nivel_data["coches"]

            self.nivel = nivel

            return True

        except Exception:
            print(f"Error al cargar el nivel {nivel}")
            return False

    def en_rango(fil, col) -> bool:
        # TODO Comprueba si la casilla es valida
        pass

    def crea_coches(let, txt) -> Coche:
        # TODO Crea un coche horizontal o vertical dependiendo de txt
        pass

    def mover_coche(self, mov) -> bool:
        # TODO metodo para procesar movimientos
        pass

    def fin_nivel(self) -> bool:
        # TODO metodo calcular fin nivel
        pass

    def __str__(self):
        # TODO metodo
        pass
