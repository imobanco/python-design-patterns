
class Pedido:

    def __init__(self, valor, tipo_entrega="normal"):
        self.__valor = valor
        self.tipo_entrega = tipo_entrega

    @property
    def valor(self):
        return self.__valor


class Entrega:

    def calcular_valor(self, pedido):
        tipos_de_entrega = {"normal": Normal(), "rapida": Rapida()}

        try:
            tipo = tipos_de_entrega[pedido.tipo_entrega]
        except KeyError:
            return print ("tipo de entrega não reconhecido")

        total = tipo.calcular(pedido)
        print(total)

class Normal:
    def calcular(self, pedido):
        return pedido.valor * 0.05

class Rapida:
    def calcular(self, pedido):
        return pedido.valor * 0.1

print("Exemplo com entrega rapida")
pedido1 = Pedido(valor=500, tipo_entrega="rapida")
print(f"valor do pedido:{pedido1.valor}, tipo de entrega: {pedido1.tipo_entrega}")
print("valor da entrega:", Entrega().calcular_valor(pedido1))

print("Exemplo com entrega não especificada")
pedido2 = Pedido(valor=500)
print(f"valor do pedido:{pedido2.valor}, tipo de entrega: {pedido2.tipo_entrega}")
print("valor da entrega:", Entrega().calcular_valor(pedido2))

print("Exemplo com entrega que nao existe")
pedido3 = Pedido(valor=500, tipo_entrega="errada")
print(f"valor do pedido:{pedido3.valor}, tipo de entrega: {pedido3.tipo_entrega}")
print("valor da entrega:", Entrega().calcular_valor(pedido3))

print("Exemplo com entrega normal")
pedido4 = Pedido(valor=500, tipo_entrega="normal")
print(f"valor do pedido:{pedido4.valor}, tipo de entrega: {pedido4.tipo_entrega}")
Entrega().calcular_valor(pedido4)