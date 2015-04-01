class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.account_history = ["Account was created"]

    def history(self):
        return self.account_history

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount
            deposit_history = 'Deposited ' + str(amount) + self.currency
            self.account_history.append(deposit_history)

    def itsbalance(self):
        balance_history = 'Balance check -> ' + str(self.balance) + self.currency
        self.account_history.append(balance_history)
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            withdraw_history = str(amount) + self.currency + ' was withdrawed'
            self.account_history.append(withdraw_history)
            return True
        else:
            withdraw_history = 'Withdraw for {}{} failed.'.format(
                amount, self.currency)
            self.account_history.append(withdraw_history)
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        int_history = '__int__ check -> ' + str(self.balance) + self.currency
        self.account_history.append(int_history)
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        if self.balance < amount:
            return False
        account1 = 'Transfer to {} for {}{}'.format(
            account.name, amount, self.currency)
        account2 = 'Transer from {} for {}{}'.format(
            self.name, amount, account.currency)
        self.account_history.append(account1)
        account.account_history.append(account2)
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
print(account.history())
