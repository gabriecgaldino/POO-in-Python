# Simulação de um Banco

Vamos criar uma aplicação bancária implementando os conceitos aprendidos até o momento. A idéia aqui é garantir o uso dos pilares da POO e dos conceitos de SOLID. Mais detalhes serão acrescentados conforme o desenvolvimento da aplicação.

## Classe Conta

A classe 'Conta' é definida para definir os atributos básicos de uma conta bancária, é importante salientar que por estarmos levando em consideração os conceitos aprendidos nos commits anteriores, separamos as atribuições da Conta em Transação e Operação.

    * Transação
    A transação possui os dados mínimos para realização de uma operadora. 

    * Operação
    As operações possuem os métodos necessários para realização de entradas e saídas no saldo da conta.

As operações herdam os atributos de Transação, então toda vez que uma nova operação for criada, podemos usar os atributos e os métodos nativos de Operação. Também é importante enfatizar que a Conta não possui operações nativamente, sendo assim, toda vez que uma operação precisar ser realizada, uma nova Operação será criada.