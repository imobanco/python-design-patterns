from observer_abc import Observador, Observavel

class BolaDeCristal(Observavel):
    def atualizar(self, mensagem):
        print(f"Fausto está na escola, mas recebeu a mensagem: {mensagem}")

class Centauro(Observador):
    ...

class Unicornio(Observador):
    ...

unicornio = Unicornio()
unicornio.adicionar_observer(BolaDeCristal())
unicornio.notificar_observers('Os mortos chegaram #medo')


centauro = Centauro()
centauro.adicionar_observer(BolaDeCristal())
centauro.notificar_observers('Os mortos chegaram #medo')
