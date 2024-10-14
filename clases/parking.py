from .coche import Coche
from .cocheH import CocheH
from .cocheV import CocheV
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
                self.coches.clear()
                for c in nivel_data["coches"]:
                    self.coches.append(self.crea_coches(len(self.coches), c))

            self.nivel = nivel

            return True

        except Exception as e:
            print(f"Error al cargar el nivel {nivel}: ", e)
            return False

    def en_rango(fil, col) -> bool:
        # TODO Comprueba si la casilla es valida
        pass

    def crea_coches(self, num_c: int, txt: str) -> Coche:
        let: chr = chr(num_c + 65)

        return CocheV(let, txt) if txt[0] == "V" else CocheH(let, txt)

    def mover_coche(self, mov) -> bool:
        # TODO metodo para procesar movimientos
        pass

    def fin_nivel(self) -> bool:
        # TODO metodo calcular fin nivel
        pass

    def __str__(self) -> str:
        p = [["#" if (c == 0 or c == self.columnas+1) or (f == 0 or f == self.filas+1) else " " for c in range(self.columnas+2)] for f in range(self.filas+2)]
        p[self.salida[0]][self.salida[1]] = " "

        for coche in self.coches:
            coord = [coord for coord in coche]
            letras = list(f"{coche}")

            for _ in range(len(coord)):
                c = coord.pop(0)
                p[c[0]][c[1]] = letras.pop(0)


        cadena = ""
        for l in p:
            cadena += " ".join(l)
            cadena += "\n"
        return cadena