# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE "OPEN\CLOSED PRINCIPLE" (OCP)

# O software deve estar aberto para extensão, mas fechado para modificação. 

# Isso significa que você não deve alterar o código existente para adicionar funcionalidades, ao invés disso você extende.

from dataclasses import dataclass

#EXEMPLO INCORRETO
# Adicionar um if, elif para cada tipo, tornará o código poluído e inviável a longo prazo.
def calcular_preco(tipo):
    if tipo == 'regular': 
        return 10
    elif tipo == 'vip':
        return 20
    
@dataclass
# Para isso adicionamos uma classe Pai(Ingresso) que não tem retorno e servirá como uma espécie de interface para as demais classes. 
class Ingresso:
    def preco(self):
        pass

# Agora, temos uma classe Regular que herda os métodos de Ingresso. Dessa forma, definimos como o comportamento de 'preco' ocorrerá.
class Regular(Ingresso):
    def preco(self):
        return 10

class Vip(Ingresso):
    def preco(self):
        return 20

# Para finalizar, utilizamos um método que irá receber como parâmetro o a Classe em questão.
def mostrar_preco(ingresso):
    print(f'Preço: R${ingresso.preco()}')  


mostrar_preco(Vip())
mostrar_preco(Regular())

# Saída esperada: Preço: R$20 & Preço: R$10


# Conclusão: Com o conceito de OCP, garantimos a mantenebilidade, organização e legibilidade do código, garantindo que atualizações não interfiram 
# no que já está definido.
#  
