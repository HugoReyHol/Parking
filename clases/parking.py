from coche import Coche

class Parking:
    coches: list[Coche] = []
    nivel: int = 0

    def __init__(self, niveles_json: str):
        self.niveles_json = niveles_json
