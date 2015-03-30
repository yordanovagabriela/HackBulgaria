class BankAccount:


    def __init__(self, name, balance, currency,amount):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.amount = amount


    def deposit(self):
        self.balance += self.amount

    def balance(self):
        return self.balance


    def withdraw(self):
        if self.amount <= self.balance:
            return True
            self.balance -= self.amount
        else:
            return False


    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name,self.amount,self.currency)


    def __int__(self):
        return self.balance


    def transfer_to(account,amount):
        if self.currency != account.currency:
            return False


account = BankAccount("Rado", 0, "$")
print(account)
print(account.deposit(1000))
print(account.balance())
print(str(account))
print(int(account))

