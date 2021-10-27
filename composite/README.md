# Composite 
#### Árvore de objetos, Object tree

O Composite é um padrão de projeto estrutural que organiza objetos em uma estrutura de árvore, permitindo tratar diferentes objetos da mesma maneira.  
Ele pode possuir classes distintas, desde que estejam organizadas em hierarquia.  Cada objeto composite possui um método para tratar seus filhos.

Foi usado como exemplo uma empresa composta por departamentos que são compostos por funcionários.

- Funcionário: Representa o objeto folha, a folha não tem nenhum componente filho.
- Departamento e Empresa: Armazena o componente filho e implementa funções relacionadas ao componente filho.

## Para rodar os exemplos:
``` 
python composite/empresa.py  
```

### Referências:
- https://refactoring.guru/pt-br/design-patterns/composite/python/example
- https://www.geeksforgeeks.org/composite-method-python-design-patterns/


