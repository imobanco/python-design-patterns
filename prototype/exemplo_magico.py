
class Animal:
    def __init__(self, nome=''):
        self.nome = nome

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)

        try:
            source: Animal = kwargs['source']
            obj.nome = source.nome
        except KeyError:
            pass

        return obj

    def __str__(self):
        return f"{self.__class__.__name__} {id(self)}, nome {self.nome}"

    def clone(self):
        return self.__new__(self.__class__, source=self)


class Cachorro(Animal):

    def __init__(self, pedigree='', nome=''):
        super().__init__(nome)
        self.pedigree = pedigree

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)

        try:
            source: Cachorro = kwargs['source']
            obj.pedigree = source.pedigree
        except KeyError:
            pass

        return obj

    def __str__(self):
        return f"{self.__class__.__name__} {id(self)}, nome {self.nome}, pedigree {self.pedigree}"


class Gato(Animal):
    def __init__(self, raca='', nome=''):
        super().__init__(nome)
        self.raca = raca

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)

        try:
            source: Gato = kwargs['source']
            obj.raca = source.raca
        except KeyError:
            pass

        return obj

    def __str__(self):
        return f"{self.__class__.__name__} {id(self)}, nome {self.nome}, raca {self.raca}"


if __name__ == '__main__':
    print("Exemplo!")

    animal1 = Animal()
    animal1.nome = 'Coragem'

    gato1 = Gato()
    gato1.nome = 'Garfield'
    gato1.raca = 'Sphinx'

    cachorro1 = Cachorro()
    cachorro1.nome = "Rex"
    cachorro1.pedigree = "Doberman"

    originais = [
        animal1, gato1, cachorro1
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
