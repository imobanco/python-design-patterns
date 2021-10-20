# Chain of Responsibility
De acordo com o Refactoring Guru o Chain of Responsibility é um padrão de projeto comportamental que permite que você passe pedidos por uma corrente de handlers. Ao receber um pedido, cada handler decide se processa o pedido ou o passa adiante para o próximo handler na corrente.

Foi usado como exemplo uma loja que possui carrinho e itens para serem adicionados ao carrinho.
A loja possui duas promoções:
- 10% quando o carrinho possuir mais de 5 itens.
- 30% quando o valor total em compra do carrinho for acima de 1000

Ao processar o calculo final da compra o pedido passará pelos handlers(promoções), que decidirão 
se vão dar uma resposta para o pedido ou não, caso não, o pedido será passado para o próximo handler.

## Para rodar os exemplos:
``` 
python chain-of-responsibility/loja1.py  
```

### Fontes:
- https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility

- https://www.youtube.com/watch?v=fG5pYDVm8_M

- https://www.youtube.com/watch?v=iqVOUAbeGoE

