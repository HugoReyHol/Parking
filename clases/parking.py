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
    def cargar_nivel(self, nivel: int):
        # TODO lectura del nivel
        pass

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