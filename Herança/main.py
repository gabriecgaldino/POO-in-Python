# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE HERANÇA(POO) EM PYTHON

#   Vamos criar uma Classe pai com atributos e métodos que serão acessados pelas subclasses. 
#   Depois vamos criar um exemplo de herança múltipla.
#   Para terminar, vamos instanciar essas classes e verificar o que acontece. 

from dataclasses import dataclass

@dataclass
class Veiculo():
    marca: str
    ano: int
    cavalos: int

    def liga(self):
        print('Motor ligado...')

    def desliga(self):
        print('Motor desligado...')

class Ação():
    def acelerar(self):
        print('Acelerando o motor...')
    def freiar(self):
        print('Freiando...')

# Aqui criamos a classe Piloto que herda Veículo e Ação
class Piloto(Veiculo, Ação):
    def entrar(self):
        print('Dentro do carro!')

    def sair(self):
        print('Fora do carro!')
    
# Aqui criamos uma instancia da classe Piloto que herda todos os métodos de Veiculo e Ação. 
player1 = Piloto('Ford', 1998, 350)


print(player1)
player1.entrar() #Método nativo da Classe
player1.liga() #Método herdado de Veiculo
player1.acelerar() #Método herdado de ação
player1.freiar() #Método herdado de ação
player1.desliga() #Método herdado de Veiculo
player1.sair() #Método nativo da Classe.

#Conclusão: Com isso podemos ver como é fácil acessar métodos de herança única e de herança múltipla a partir de uma subclasse. 


