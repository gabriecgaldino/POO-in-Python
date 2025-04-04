# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE "SINGLE RESPONSIBILITY PRINCIPLE" (SRP)

# Uma classe deve ter apenas um motivo para mudar, ou seja, uma única responsabilidade. 
# A seguir apresento um exemplo do conceito. 

from dataclasses import dataclass

# CASO DE USO DA MANEIRA INCORRETA A SE ESCREVER AS CLASSES.
@dataclass
#Aqui temos uma classe usuário que deveria ser responsável apenas pelas ações do usuário.
class Usuario:
    nome: str
    saldo: float

    # Como por exemplo salvar o usuário no banco de dados.
    def salvar(self):
        print(f'Salvando {self.nome} no banco....')

    # O método atualizar saldo, acaba bagunçando a lógica por traz do sistema, o correto seria garantir que uma nova classe existisse garantindo
    # que o sistema esteja organizado e legível. 
    def atualizar_saldo(self, valor):
        if valor > 0:
            saldo_novo = self.saldo + valor
            print(f'Saldo atualizado R$ {saldo_novo}')


# EXEMPLO CORRETO DE COMO O MESMO CASO DEVERIA SER ESCRITO.

@dataclass
# Agora temos uma classe conta que é reponsável por atribuir o saldo do usuário e realizar as atualizações necessárias, garantindo que o código 
# esteja claro e legível.
class Conta:
    saldo: float

    # Método responsável por realizar a atualização de saldo. 
    def atualizar_saldo(self, valor):
        if valor > 0:
            saldo_novo = self.saldo + valor
            print(f'Saldo atualizado R$ {saldo_novo}')

# Exemplo 1 - Atributo que acessa o objeto conta e tem acesso ao saldo.
# Classe usuário, separando as responsábilidades do sistema. 
class Usuario:
    nome: str
    conta: Conta

    def salvar(self):
        print(f'Salvando {self.nome} no banco....')

saldo = Conta(150.99)
usuario1 = Usuario('Galdino', saldo)

# Exemplo 2 - A classe usuário herda os métodos e atributos da Classe conta. 
class Usuario(Conta):
    nome: str

    def salvar(self):
        print(f'Salvando {self.nome} no banco....')


usuario2 = Usuario('galdino')
usuario2.saldo = 150.99