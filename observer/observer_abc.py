from abc import ABC, abstractmethod, abstractproperty
from typing import List

class Observavel(ABC):
    """Feitiço para objetos que querem ser observados."""

    @abstractmethod
    def atualizar(self):
        ...

    @property
    @abstractmethod
    def observers() -> List:
        ...

    @abstractmethod
    def adicionar_observer(self, observer):
        ...

    @abstractmethod
    def notificar_observers(self, mensagem):
        ...

class Observador(ABC):
    """Súditos que observam algo!""""

    @abstractmethod
    def receber_notificacao(self, mensagem):
        ...
