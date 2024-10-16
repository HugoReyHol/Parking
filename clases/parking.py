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
    # Recibe el número del nivel a cargar
    # Devuelve True si ha cargado correctamente, si no False
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
                    self.coches.append(self.__crea_coches(len(self.coches), c))

            self.nivel = nivel

            print(f"Nivel {nivel}:")

            return True

        except Exception as e:
            print(f"Error al cargar el nivel {nivel}: ", e)
            return False

    # Comprueba si el movimiento está dentro del parking
    # Recibe una tupla con el movimiento a comprobar
    # Devuelve True si está dentro de los límites o False si está fuera
    def __en_rango(self, pos: tuple[int, int]) -> bool:
        return (pos[0] in range(1, self.filas+1) and pos[1] in range(1, self.columnas+1)) or pos == self.salida

    # Crea un coche dependiendo de su tipo
    # Recibe el número del cocho y el texto con sus características
    # Devuelve un CocheV o un CocheH dependiendo del texto
    def __crea_coches(self, num_c: int, txt: str) -> Coche:
        let: chr = chr(num_c + 65)

        return CocheV(let, txt) if txt[0] == "V" else CocheH(let, txt)

    # Mueve el coche con el comando indicado,
    # Recibe una letra con el movimiento
    # Devuelve True si se puede mover y si no False
    def mover_coche(self, mov: chr) -> bool:
        try:
            coche: Coche = next(filter(lambda c: str(mov).upper()[0] == c.letra, self.coches))

        except StopIteration:
            print(f"Movimiento no válido, no hay un coche {str(mov).upper()}")
            return False

        pos = coche.calcular_espacio(str(mov).isupper())

        coords = [coord for c in self.coches for coord in c if c.letra != str(mov).upper()]
        # Si no está en rango sale de la funcion
        if (not self.__en_rango(pos)) or (pos in coords):
            return False

        coche.mover(str(mov).isupper())

        return True

    # Comprueba si la posicion de salida está en las coordenadas del primer coche
    # Devuelve True si es así, si no False
    def fin_nivel(self) -> bool:
        return self.salida in [coord for coord in self.coches[0]]
        pass

    # Cambia el formato en el que se devuelve el parking al imprimirlo
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