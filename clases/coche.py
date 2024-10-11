from abc import ABC, abstractmethod


class Coche(ABC):

    # Constructor del coche generico
    def __init__(self, letra: chr, posicion: list[int], largo: int):
        self.letra = str(letra).upper()[0]
        self.posicion = posicion
        self.largo = largo

    # Metodos abstractos que serán sobreescritos en sus hijos
    @abstractmethod
    def mover(self, direccion: chr) -> bool:
        pass

    @abstractmethod
    def comprobar_espacio(self, direccion: chr) -> list[int]:
        pass

    @abstractmethod
    def devolver_casillas(self, direccion: chr) -> list[list[int]]:
        pass
