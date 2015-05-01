class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.amount)


class BatchBill(Bill):

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum(self.bills)

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk():

    def __init__(self):
        self.desk = []

    def take_money(self, money):
        self.desk.append(money)

    def total(self):
        total_sum = 0
        for money in self.desk:
            total_sum += int(money)
        return total_sum

    def inspect(self):
        for batch in self.desk:
            for bill in batch:
                print(str(bill))
