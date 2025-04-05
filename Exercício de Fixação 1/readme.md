# Simulação de um Banco

Vamos criar uma aplicação bancária implementando os conceitos aprendidos até o momento. A idéia aqui é garantir o uso dos pilares da POO e dos conceitos de SOLID. Mais detalhes serão acrescentados conforme o desenvolvimento da aplicação.

## Classe Conta

A classe 'Conta' é definida para definir os atributos básicos de uma conta bancária, é importante salientar que por estarmos levando em consideração os conceitos aprendidos nos commits anteriores, separamos as atribuições da Conta em Transação e Operação.

    * Transação
    A transação possui os dados mínimos para realização de uma operadora. 

    * Operação
    As operações possuem os métodos necessários para realização de entradas e saídas no saldo da conta.

As operações herdam os atributos de Transação, então toda vez que uma nova operação for criada, podemos usar os atributos e os métodos nativos de Operação. Também é importante enfatizar que a Conta não possui operações nativamente, sendo assim, toda vez que uma operação precisar ser realizada, uma nova Operação será criada.

## Classe Usuário

A classe 'Usuário' possui os atributos mínimos para o exemplo que iremos desenvolver, com isso criamos mais duas classes para auxliar na abstração dos casos de uso: 'Titular' e 'Dependente'. Os tipos de produtos e operações que podem ser realizadas por um usuário, serão definidos posteriormente. 

    * Titular
    A classe Titular herda todos os atributos de Usuario, porém como existem dois tipos de usuario em nosso sistema, separamos as classes para maior flexibilidade. 

    * Dependente
    A classe Dependente também herda todos os atributos de Usuario, porém, esta possui um atributo diferente: titular, que funciona como uma espécie de chave estrangeira para ligar as contas dependentes as contas titulares.
    