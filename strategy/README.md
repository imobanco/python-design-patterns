# Strategy

Strategy é um dos padrões mais populares e simples de ser compreendido. Ele permite que o algoritmo varie independentemente de quem o utiliza.
O comportamento é bem parecido com Template Method, mas enquanto Template Method usa herança, o Strategy usa delegação/composição.

Como exemplo foi criado o objeto Pedido que possui dois tipos de entrega (normal e rápida).
O calculo da entrega normal e rápida possui a mesma fórmula, sendo alterado somente o valor e tipo.
Então para evitar duplicidade de código foi utilizado padrão strategy e criado o método Entrega, 
que ao receber o valor e o tipo de pedido retornará o calculo do frete. 


## Fontes:

- https://stackoverflow.com/questions/669271/what-is-the-difference-between-the-template-method-and-the-strategy-patterns
- https://refactoring.guru/pt-br/design-patterns/strategy