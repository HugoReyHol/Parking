from .coche import Coche


class CocheV(Coche):

    # Calcula el movimiento VERTICALMENTE
    def mover(self, direccion: chr) -> bool:
        # TODO metodo
        pass

    # Calcula el espacio al que se va a mover VERTICALMENTE
    # Para moverse hacia delante dirreccion es true y marcha atras es false
    def calcular_espacio(self, direccion: bool) -> tuple[int, int]:
        return (self.pos[0]-1, self.pos[1]) if direccion else (self.pos[0]+self.tam, self.pos[1])

    # Calcula el espacio que ocupa el coche VERTICALMENTE
    def __iter__(self):
        # TODO metodo
        pass

    def __str__(self):
        # TODO metodo
        pass
