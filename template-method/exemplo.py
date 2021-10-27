from abc import ABC, abstractmethod

class PrepararBebida(ABC):
    def preparar_bebida(self):
        print(self.aquecer_agua())
        print(self.adicionar_mistura())
        print(self.colocar_no_copo())

    def aquecer_agua(self):
        return ("aquecendo agua")

    @abstractmethod
    def adicionar_mistura(self):
        pass

    def colocar_no_copo(self):
        return ("colocando no copo")


class Cafe(PrepararBebida):
    def adicionar_mistura(self):
        return ("adicionando Café")

class Cha(PrepararBebida):
    def adicionar_mistura(self):
        return ("adicionar chá")

class Chocolate(PrepararBebida):
    def adicionar_mistura(self):
        return ("adicionar chocolate")


cafe = Cafe()
cafe.preparar_bebida()

print("---------------------")

cha = Cha()
cha.preparar_bebida()

print("---------------------")

chocolate = Chocolate()
chocolate.preparar_bebida()
