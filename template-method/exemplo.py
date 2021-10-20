class Animal:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

class Pelo(Animal):
    def __init__(self, tipo, tamanho):
        self.tipo = tipo
        self.tamanho = tamanho

    def __repr__(self):
        return self.tipo

class Falar(Animal):
    def __init__(self, fala):
        self.fala = fala

    def __repr__(self):
        return (f"{Animal}:{self.fala}")

class Patas(Animal):
    def __init__(self, quantidade):
        self.quantidade = quantidade
    def __repr__(self):
        return self.quantidade

class Cor(Animal):
    def __init__(self, cor):
        self.cor = cor

    def __repr__(self):
        return self.cor




cachorro = Animal(nome="Cachorro")

fala = Falar(cachorro)