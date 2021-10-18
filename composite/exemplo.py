from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    A classe base Component declara operações comuns para objetos simples e
     complexos de uma composição.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Opcionalmente, o componente base pode declarar uma interface para configuração e
         acessar um pai do componente em uma estrutura de árvore. Também pode
         fornecer alguma implementação padrão para esses métodos.
        """

        self._parent = parent

    """
    Em alguns casos, seria benéfico definir o manejo da operação filho para à direita na 
    classe base Component. Dessa forma, você não precisará expor quaisquer classes de 
    componentes concretos para o código do cliente, mesmo durante o montagem da árvore de objetos. 
    A desvantagem é que esses métodos estarão vazios para os componentes de nível folha(leaf).
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Você pode fornecer um método que permite ao código do cliente descobrir se um
         componente pode ter filhos.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        O componente base pode implementar algum comportamento padrão ou deixá-lo para
         classes concretas (declarando o método que contém o comportamento como
         "abstrato").
        """

        pass


class Folha(Component):
    """
    A classe Folha(Leaf) representa os objetos finais de uma composição.
    Uma folha não pode ter filhos.
     Normalmente, são os objetos Folha(Leaf) que fazem o trabalho real, enquanto
     Composite objetos apenas delegam a seus subcomponentes.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    A classe Composite representa os componentes complexos que podem ter
     filhos. Normalmente, os objetos Composite delegam o trabalho real aos seus
     filhos e, em seguida, "resumir" o resultado.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    Um objeto composto pode adicionar ou remover outros componentes (simples ou
     complexo) para ou de sua lista de filhos.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        O Composite executa sua lógica primária de uma maneira particular. Isto
         atravessa recursivamente todos os seus filhos, coletando e somando
         seus resultados. Uma vez que os filhos do composto passam essas chamadas para seus
         filhos e assim por diante, toda a árvore de objetos é percorrida como resultado.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    O código do cliente funciona com todos os componentes por meio da interface base.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
