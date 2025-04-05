from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Transacao:
    __valor: float
    __data: datetime
    __tipo: bool

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self):
        self.__data = date.today()

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self):
        """True = Entrada & False = Saída"""
        if self.__tipo: 
            self.__tipo = False
        else: 
            self.__tipo = True 

@dataclass
class Operacao(Transacao):
    def deposito(self, valor):
        if valor > 0:
            self.saldo = valor
        else:
            raise Exception('Impossível realizar um depósito de valor negativo.')
    
    def saque(self, valor):
        if valor > self.saldo:
            raise Exception(f'Saldo insulficiente: R$ {self.saldo}.')
        else:
            self.saldo = valor


@dataclass
class Conta:
    __saldo: float
    __data_abertura: date
    __status: bool

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            self.__saldo -= valor
    @property
    def data_abertura(self):
        return self.__data_abertura
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self):
        """True = Ativa & False = Inativa"""
        if self.__status:
            self.__status = False
        else:
            self.__status = True