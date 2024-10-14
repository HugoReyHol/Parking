from collections.abc import Iterator
from .coche import Coche


class CocheH(Coche):
    # Calcula el movimiento HORIZONTALMENTE
    def mover(self, direccion: chr) -> bool:
        # TODO metodo
        pass

    # Calcula el espacio al que se va a mover HORIZONTALMENTE
    # Para moverse hacia delante dirreccion es true y marcha atras es false
    def calcular_espacio(self, direccion: bool) -> tuple[int, int]:
        return (self.pos[0], self.pos[1]-1) if direccion else (self.pos[0], self.pos[1]+self.tam)

    # Crea un generador con las casillas que ocupa el coche HORIZONTALMENTE
    def __iter__(self) -> Iterator:
        return ((self.pos[0], self.pos[1]+i) for i in range(self.tam))

    def __str__(self) -> str:
        return self.letra + "═"*(self.tam-2) + chr(ord(self.letra) + 32)