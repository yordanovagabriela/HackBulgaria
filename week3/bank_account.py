class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount

    def itsbalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            return True
            self.balance -= amount
        else:
            return False
        self.balance -= self.amount

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        if self.balance < amount:
            return False
        self.balance -= amount
        account.balance += amount
        return True

account = BankAccount("Rado", 0, "$")
print(account)
print(account.deposit(2000))
print(account.itsbalance())
print(str(account))
print(int(account))
print(account.withdraw(2000))
rado = BankAccount("Rado", 600, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 700))
print(rado.balance)
print(ivo.balance)

