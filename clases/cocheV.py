from collections.abc import Iterator
from .coche import Coche


class CocheV(Coche):

    # Realiza el movimiento VERTICALMENTE
    def mover(self, direccion: bool) -> None:
        self.pos = (self.pos[0]-1 if direccion else self.pos[0]+1, self.pos[1])

    # Calcula el espacio al que se va a mover VERTICALMENTE
    # Para moverse hacia delante dirreccion es true y marcha atras es false
    def calcular_espacio(self, direccion: bool) -> tuple[int, int]:
        return (self.pos[0]-1, self.pos[1]) if direccion else (self.pos[0]+self.tam, self.pos[1])

    # Crea un generador con las casillas que ocupa el coche VERTICALMENTE
    def __iter__(self) -> Iterator:
        return ((self.pos[0]+i, self.pos[1]) for i in range(self.tam))

    def __str__(self) -> str:
        return self.letra + "║"*(self.tam-2) + chr(ord(self.letra) + 32)