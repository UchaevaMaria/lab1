class BankAccount: #создаем класс
    def __init__(self, initial_balance=0): #иниц, начальный баланс принимаем за ноль
        self._balance = initial_balance #нижнее подчеркивание реализует приватность
        self._transactions = [] 
    def deposit(self, amount): #счет
        if amount > 0:
            self._balance += amount #прибавляем к балансу
            self._transactions.append(amount)  #логируем, отслеживаем
            print("внесено", amount, "текущий баланс:", self._balance) #для проверки 
    def withdraw(self, amount):
        if amount > 0: #cумма для снятия должна быть больше нуля
            if amount <= self._balance: # и не больше самого баланса
                self._balance -= amount
                self._transactions.append(amount)  #логируем
                print("снято", amount, "текущий баланс", self._balance)
            else:
                print("недостаточно средств :(")
        else:
            print("0 cнять не получится, хотя бы рубль")
    @property #как к атрибуту
    def balance(self):
        return self._balance  # Геттер для доступа к балансу

    def get_transactions(self):
        return self._transactions
#проверка 
account = BankAccount(1000)
account.deposit(50)
account.withdraw(190)
for transaction in account.get_transactions():
    print(transaction)
print("Текущий баланс:", account.balance)  # геттер balance