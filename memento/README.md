# Memento


Memento é um design patter comportamental que permite fazer snapshots instantâneos do estado 
de um objeto e restaurá-los no futuro.

O Memento não compromete a estrutura interna do objeto com o qual trabalha, bem como os dados 
mantidos dentro dss snapshots.

Exemplos de uso: o princípio do Memento pode ser alcançado usando a serialização, que é bastante
comum em Python. Embora não seja a única e mais eficiente maneira de fazer snapshots do 
estado de um objeto, este padrão permite armazenar backups de estado, protegendo a estrutura 
do originador de outros objetos.


## Rodar os exemplos

```bash
python memento/exemplo_1.py
```

```bash
python memento/exemplo_2.py
```

## Referências

- https://refactoring.guru/design-patterns/memento
- https://www.geeksforgeeks.org/memento-method-python-design-patterns/
