from coche import Coche


class CocheH(Coche):
    # Calcula el movimiento HORIZONTALMENTE
    def mover(self, direccion: chr) -> bool:
        # TODO metodo
        pass

    # Calcula el espacio para moverse HORIZONTALMENTE
    def comprobar_espacio(self, direccion: chr) -> list[int]:
        # TODO metodo
        pass

    # Calcula el espacio que ocupa el coche HORIZONTALMENTE
    def devolver_casillas(self, direccion: chr) -> list[list[int]]:
        # TODO metodo
        pass

    def __iter__(self):
        # TODO metodo
        pass

    def __str__(self):
        # TODO metodo
        pass