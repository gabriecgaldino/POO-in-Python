from dataclasses import dataclass
from conta import Conta

@dataclass
class Usuario:
    __nome: str
    __email: str
    __cpf: str
    __ativo: bool
    __conta: Conta

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self):
        if self.__ativo:
            self.__ativo = False
        else: 
            self.__ativo = True

@dataclass
class Titular(Usuario):
    pass

class Dependente(Usuario):
    titular: Titular


    