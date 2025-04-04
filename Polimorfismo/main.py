# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE POLIMORFISMO (POO)

# A idéia do exercício é demonstrar como podemos implementar o mesmo metodo para realizar tarefas diferentes.

from dataclasses import dataclass


# Definimos uma classe carro com os atributos principais. 
@dataclass
class Carro:
    marca: str
    vel_max: int
    tempo_0x100: float = 0

    # método acelerar que possui um valor padrão para carro.
    def acelerar(self):
        self.tempo_0x100 = 15.5
        print(self.tempo_0x100)
    
# Aqui criamos uma nova categoria de carro(esportivo) mas que herda os atributos e métodos de carro.
class Carro_Esportivo(Carro):
    # Porém por se tratar de um carro esportivo, o carro também precisa de um método acelerar mas que se comporta de maneira diferente.
    def acelerar(self):
        self.tempo_0x100 = 2.5
        print(self.tempo_0x100)
    
# Instanciamos os dois objetos
carro1 = Carro('Ford', 240)
carro2 = Carro_Esportivo('McLaren', 320)

# Chamamos o mesmo método para cada um dos objetos instanciados. 
carro1.acelerar()
carro2.acelerar()

# Saída Esperada: 15.5 e 2.5

