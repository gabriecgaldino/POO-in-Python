# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE DEPENDENCY INVERSION PRINCIPLE (DIP)

# Dependa de abstrações, não de implementações concretas. Uma classe não deve depender de detalhes. Invertemos a dependência injetando as implementações
# por fora.

# EXEMPLO INCORRETO
# Aqui temos um método de salvamento de um dado no banco de dados mysql.
class MySqlDatabase:
    def salvar(self, dado):
        print(f'Salvando no MySql: {dado}.')

# O problema é que por padrão, Usuário service espera explicitamente salvar o MySQLDatadase. 
class UsuarioService:
    def __init__(self):
        self.db = MySqlDatabase() #acoplado


#EXEMPLO CORRETO
class BancoDeDados:
    def salvar(self, dado): pass

class MySqldataBase(BancoDeDados):
    def salvar(self, dado):
        print(f'Salvando no MySQL: {dado}.')

# Já aqui, o UsuarioService não se importa com o tipo de banco de dados. Só espera um banco de dados. 
class UsuarioService:
    def __init__(self, banco: BancoDeDados):
        self.db = banco

    def registrar(self, usuario):
        self.db.salvar(usuario)

# Injeção de depêndencia:

mysql = MySqlDatabase()
# Ao injetar as dependencias que será definido o tipo de banco de dados onde será salvo.
service = UsuarioService(mysql)
service.registrar("João")

    