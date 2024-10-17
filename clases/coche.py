from abc import ABC, abstractmethod


class Coche(ABC):

    # Constructor del coche generico
    def __init__(self, letra: chr, txt: str):
        self.letra = letra
        self.pos = (int(txt[1]), int(txt[2]))
        self.tam = int(txt[3])

    # Metodos abstractos que serán sobreescritos en sus hijos
    @abstractmethod
    def mover(self, direccion: bool) -> None:
        pass

    @abstractmethod
    def calcular_espacio(self, direccion: bool) -> tuple[int, int]:
        pass
