from abc import ABC, abstractmethod


class Animal(ABC):
    nome: str

    def __init__(self, source=None):
        if source:
            self.nome = source.nome

    def __str__(self):
        return f"Animal {id(self)}, nome {self.nome}"

    @abstractmethod
    def clone(self):
        pass


class Cachorro(Animal):
    pedigree: str

    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.pedigree = source.pedigree

    def __str__(self):
        return f"Cachorro {id(self)}, nome {self.nome}, pedigree {self.pedigree}"

    def clone(self):
        return Cachorro(self)


class Gato(Animal):
    raca: str

    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.raca = source.raca

    def __str__(self):
        return f"Gato {id(self)}, nome {self.nome}, raca {self.raca}"

    def clone(self):
        return Gato(self)


if __name__ == '__main__':
    print("Exemplo!")

    gato1 = Gato()
    gato1.nome = 'Garfield'
    gato1.raca = 'Sphinx'

    gato2 = gato1.clone()

    cachorro1 = Cachorro()
    cachorro1.nome = "Rex"
    cachorro1.pedigree = "Doberman"

    originais = [
        gato1, cachorro1
    ]

    print('Originais:')
    for original in originais:
        print(original)

    clones = [
        original.clone() for original in originais
    ]

    print('Clones:')
    for clone in clones:
        print(clone)
