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


new_bill = Bill(20)
second_bill = Bill(50)

money_holder = {}

money_holder[a] = 1 # We have one 10% bill

if c in money_holder:
    money_holder[c] += 1

print(money_holder) # { "A 10$ bill": 2 }
print(str(new_bill))
print(int(new_bill))
print(new_bill)
print(new_bill == second_bill)
print(hash(new_bill))



class BatchBill(Bill):
    def __init__(self,bills):
        self.bills = bills
    def __len__(self):
        return len(bills)
    def total(self):
        return sum(bills)
    def __getitem__(self, index):
        return self.bills[index]

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

for bill in batch:
    print(bill)

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


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total()) # 390
desk.inspect()
