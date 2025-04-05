# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE INTERFACE SEGREGATION PRINCIPLE (ISP)

# Uma classe não deve ser forçada a depender de métodos que ela não usa. 

#EXEMPLO INCORRETO
# Aqui definimos uma classe trabalhador que possui os métodos trabalhar e comer.
class Trabalhador:
    def trabalhar(self): pass
    def comer(self): pass

# O problema é que na classe Robo, robo não come. Sendo assim, precisamos definir um método desnecessário para o uso da classe.
class Robo(Trabalhador):
    def trabalhar(self): print('Trabalhando')
    def comer(self): pass # Robô não come!

#EXEMPLO CORRETO DO USO DE INTERFACES.

# Aqui separamos as interfaces para garantir que os métodos necessários sejam atribuídos posteriormente.
class Trabalhavel:
    def trabalhar(self): pass

class Comivel:
    def comer(self): pass

# Agora, podemos dizer que a classe Humano, trabalha e come, dessa forma, irá herdar as duas classes anteriormente definidas.
class Humano(Trabalhavel, Comivel):
    def trabalhar(self): print('Humano trabalhando')
    def comer(self): print('Humano comendo')

# Um robo não precisa comer, então iremos herdar apenas trabalhavel.
class Robo(Trabalhavel):
    def trabalhar(self): print('Robo trabalhando')