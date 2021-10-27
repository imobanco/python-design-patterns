class Funcionario:
    """Classe que representa a Folha da árvore hierárquica."""
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

class Departamento:
    """ Classe que representa o Galho da árvore hierárquica que podem ter folhas."""
    def __init__(self, nome):
        self.nome = nome
        self._children = []

    def add(self, funcionario_ou_departamento):
        self._children.append(funcionario_ou_departamento)

    def __repr__(self):
        return self._children

class Empresa:
    """ Classe que representa o Tronco da árvore hierárquica quem pode ter galhos ou folhas."""

    def __init__(self, nome):
        self._children = []
        self.nome = nome

    def add(self, departamento_ou_funcionario):
        self._children.append(departamento_ou_funcionario)



print ("--Exemplo--")

f1 = Funcionario(nome="Ana")
f2 = Funcionario(nome="Maria")
f3 = Funcionario(nome="Luiz")
d1 = Departamento(nome="RH")

print(f"três funcionários {f1.nome, f2.nome, f3.nome} do departamento {d1.nome}")

d1.add(f1)
d1.add(f2)
d1.add(f3)

f4 = Funcionario(nome="Cesar")
f5 = Funcionario(nome="Wilson")
f6 = Funcionario(nome="Luiza")

d2 = Departamento(nome="TI")

print(f"três funcionários {f4.nome, f5.nome, f6.nome} do departamento {d2.nome}")

d2.add(f4)
d2.add(f5)
d2.add(f6)


e1 = Empresa(nome="Imobanco")

e1.add(d1)
e1.add(d2)

print(f"Os dois departamentos {d1.nome, d2.nome} pertecem a empresa {e1.nome}")
