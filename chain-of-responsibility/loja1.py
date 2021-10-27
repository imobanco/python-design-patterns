from typing import Callable

class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f'Item({self.nome}, {self.valor})'

class Carrinho:
    def  __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))

""" Handlers: Onde vai ser decidido se a operação acaba ou não """
def promocao_30(carrinho: Carrinho):
    if carrinho.valor > 1000:
        return carrinho.valor - (carrinho.valor * 0.3)
    raise ValueError("Promoção não executada")

def promocao_10(carrinho: Carrinho):
    if len(carrinho.itens) >= 5:
        return carrinho.valor - (carrinho.valor * 0.10)
    raise ValueError("Promoção não executada")

def sem_promocao(carrinho: Carrinho):
    return carrinho.valor

class Promocoes:
    def __init__(self, *promos: Callable):
        self.promos = promos
        self.sem_promocao = sem_promocao

    def calcular(self, valor: int):
        """
        Calcular faz o trabalho parecido com set_next,
        passando de uma promoção (handler) para outra
        """
        for promo in self.promos:
            try:
                 return promo(valor)
            except ValueError:
                 pass

        return self.sem_promocao(valor)

""" Exemplos """

c = Carrinho()

p = Promocoes(promocao_30, promocao_10, sem_promocao)

c.adicionar_item(Item('banana', 10))
c.adicionar_item(Item('banana', 10))
c.adicionar_item(Item('banana', 10))
c.adicionar_item(Item('banana', 10))
c.adicionar_item(Item('banana', 10))

print("Exemplo 1: O carrinho possui 5 itens, logo, a promoção que irá ser aplicada é a promoção de 10%")

print(f"Carinho {c.itens}")

print(f"valor original: {c.valor}")

total = p.calcular(c)

print(f"valor final: {total}")

print(total==45)

print("--------------------------------------------")

print("Exemplo 2: O valor total da compra é mais de 1000, logo, a promoção que irá ser aplicada é a promoção de 30%")

c2 = Carrinho()

c2.adicionar_item(Item('banana', 1001))

print(f"Carinho {c2.itens}")

print(f"valor original: {c2.valor}")

total = p.calcular(c2)

print(f"valor final: {total}")

print(total== 700.7)

print("--------------------------------------------")

print("Exemplo 3: O carrinho não possui 5 compras e não possui valor total de 1000, logo, não será aplicada nenhuma promoção")

c3 = Carrinho()

c3.adicionar_item(Item('banana', 1))

print(f"Carinho {c3.itens}")

print(f"valor original: {c3.valor}")

total = p.calcular(c3)

print(f"valor final: {total}")

print(total== 1)