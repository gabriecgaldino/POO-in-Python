# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE LISKOV SUBTITUTION PRINCIPLE (LSP)

# Subclasses devem poder ser substituídas por suas subclasses sem quebrar o sistema. 

from dataclasses import dataclass



#EXEMPLO INCORRETO
@dataclass
# Temos a classe Ave, que por padrão possui o método voar.
class Ave:
    def voar(self):
        pass

# Um pato voa, dessa forma, podemos definir como o método voar irá se comportar. 
class Pato(Ave):
    def voar(self):
        print('Pato voando...')

# Em contra partida, um pinguim não voa e lançará uma exceção ao chamar o método voar. 
class Pinguim(Ave):
    def voar(self):
        raise Exception('Pinguins não voam...')
    

#EXEMPLO CORRETO DE COMO DEVE SER A IMPLEMENTAÇÃO.
@dataclass
# Diferente do primeiro exemplo, aqui tratamos os métodos independentemente, para garantir que os diferentes casos de uso quebrem a lógica do sistema. 
class Ave:
    pass

class AveQueVoa(Ave):
    def voar(self):
        print('Voando...')

class AveQueNaoVoa(Ave):
    def andar(self):
        print('Andando...')

# Conclusão: Aqui, é necessário atentar-se á lógica de comportamento do sistema. As vezes, uma interface não é necessária e cada classe tem comportamentos 
# independentes. 
