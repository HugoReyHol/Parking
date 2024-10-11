from coche import Coche

class Parking:
    coches: list[Coche] = []
    nivel: int = 0

    def __init__(self, fichero_json: str):
        self.fichero_json = fichero_json
