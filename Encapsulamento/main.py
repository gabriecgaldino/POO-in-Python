# Aqui realizamos as importações necessárias de cada classe, tratar cada classe em arquivos distintos, ajuda a manter a legibilidade do código além de 
# facilitar a manutenção. 

from Account import BankAccount
from Customer import Customer


# Antes de instanciar BankAccount, é necessário criar um objeto do tipo Customer para associa-lo ao BankAccount.
customer1 = Customer('Gabriel', 'exemple@mail.com')

account1 = BankAccount(customer1, 100.50)


account1.deposity(200)
account1.withdrawal(150.50)

print(account1.balance)

