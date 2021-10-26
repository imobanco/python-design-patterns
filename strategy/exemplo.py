
class Pedido:
    def __init__(self, valor):
        self.__valor = valor
    @property
    def valor(self):
        return self.__valor


class Entrega:
    def calcular(self, pedido, entrega):
        total = entrega.calcular(pedido)
        print(total)

class Normal:
    def calcular(self, pedido):
        return pedido.valor * 0.05

class Rapida:
    def calcular(self, pedido):
        return pedido.valor * 0.1


pedido = Pedido(500)

Entrega().calcular(pedido, Normal())
Entrega().calcular(pedido, Rapida())