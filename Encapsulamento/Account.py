# EXERCÍCIO DE FIXAÇÃO DO CONCEITO DE ENCAPSULAMENTO(POO)

from dataclasses import dataclass
from Customer import Customer
import re

@dataclass
class BankAccount:
    # Aqui definimos que customer e o balance são atributos privados, ou seja, só podem ser acessados dentro da classe.
    __customer: Customer
    __balance: float

    # Com o uso de '@property', podemos definir getters e setters para garantir que os dados serão acessados por meio de métodos ao invés de diretamente,
    # isso garante que os dados estejam seguros e não hajam alterações por engano, além de ser possível garantir regras de negócio ou validação para dados
    # específicos. 

    @property
    def balance(self):
        #Docstring para garantir que o usuário entenda o que faz o método. 
        """Getter for balance."""
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """Setter for ballance."""
        if value < 0:
            return "This value can't be negative."
        else:
            self.__balance = value

    #Os métodos nativos da classe ficarão disponíveis normalmente. 
    def deposity(self, value: float):
        """Method for deposity money in account of customer"""
        if value > 0:
            self.__balance += value
            print(f'Deposity of R${value:.2f} completed. Actually Balance: R${self.__balance}')
        else:
            print('Invalid value for deposity.')
    
    def withdrawal(self, value: float):
        """Method for withdrawal money in account of customer"""
        if 0 < value <= self.__balance:
            self.__balance -= value
            print(f'Withdrawal of R${value:.2f} completed. Actually balance: R${self.__balance}')
        else:
            print('Insufficient balance or inválid value.')

    

