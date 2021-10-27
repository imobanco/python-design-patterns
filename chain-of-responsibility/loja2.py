from typing import Callable

""" E se eu quiser adicionar mais de uma promoção ? """
class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f'Item({self.nome}, {self.valor})'

class Carrinho:
    def  __init__(self):
        self.itens = []
        self.desconto = 0

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))

""" Handlers: Onde vai ser decidido se a operação acaba ou não """

def promocao_30(carrinho: Carrinho):
    if carrinho.valor >= 1000:
        carrinho.desconto += (carrinho.valor * 0.3)

def promocao_10(carrinho: Carrinho):
    if len(carrinho.itens) >= 5:
        carrinho.desconto += (carrinho.valor * 0.10)

class Promocoes:
    def __init__(self, *promos: Callable):
        self.promos = promos

    def calcular(self, carinho):
        """
        Calcular faz o trabalho parecido com set_next,
        passando de uma promoção (handler) para outra
        """

        for promo in self.promos:
            try:
                promo(carinho)
            except ValueError:
                 pass

        valor_final = carinho.valor - carinho.desconto
        return valor_final

    def adicionar_nova_promo(self, carrinho, valor):
        carrinho.desconto += (carrinho.valor * (valor/100))
        return ("promoção cadastrada")


""" Exemplos """

c = Carrinho()

p = Promocoes(promocao_30, promocao_10)

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

""" Exemplos """

c = Carrinho()

p = Promocoes(promocao_30, promocao_10)

c.adicionar_item(Item('banana', 1000))
c.adicionar_item(Item('banana', 0))
c.adicionar_item(Item('banana', 0))
c.adicionar_item(Item('banana', 0))
c.adicionar_item(Item('banana', 0))

print("Exemplo 1: O carrinho possui 5 itens e o valor total de 1000, logo será aplicado o desconto de 10% e o de 30%")

print(f"Carinho {c.itens}")

print(f"valor original: {c.valor}")

total = p.calcular(c)

print(f"valor final: {total}")

print(total==600.0)

print("--------------------------------------------")

print("Exemplo 2: O carrinho possui 5 itens e o valor total de 1000, logo será aplicado o desconto de 10% e o de 30% e uma nova promoção de 50%")

c = Carrinho()

p = Promocoes(promocao_30, promocao_10)

c.adicionar_item(Item('banana', 1000))
c.adicionar_item(Item('banana', 0))
c.adicionar_item(Item('banana', 0))
c.adicionar_item(Item('banana', 0))
c.adicionar_item(Item('banana', 0))

p.adicionar_nova_promo(c, 50)

total = p.calcular(c)

print(f"valor inicial: {c.valor}")
print(f"valor descontato: {c.desconto}")
print(f"valor final: {total}")

print(total==100.0)

print("--------------------------------------------")

