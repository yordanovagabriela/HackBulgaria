from bank_account import BankAccount
import unittest


class TestBankAccount(unnittest.TestCase):

    def test_init(self):
        my_account = BankAccount("Ivo", 100, "$")
        self.assertequal(my_account.name, "ime")

    def test_str(self):
        needed_result = BankAccount("Ivo", 100, "$")
        self.assertequal(str(my_account), needed_result)

    def test_deposite(self):
        self.my_account.deposit(100)
        self.assertequal(self.my_account.balance, 200)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)

    def test_transfer_to(self):
        your_account = BankAccount("rado", 10, "&")
        with self.assertRaises(ValueError):
            self.my_account.trasfer_to(your_account, 200)
        self.assertequal(self.my_account.balance, 10000)
        self.assertequal(self.your_account, 10)

    def transfer_more_money_than_we_have(self):
        your_account = BankAccount("rado", 10, "&")
        self.assertFalse(your_account.trasfer_to(self.my_account, 300))
        self.assertequal(self.my_account.balance, 1000000)
        self.assertequal(your_account.balance, 10)

    def test_transfer_to(self):
        your_account = BankAccount("rado", 10, "$")
        result = self.my_account.trasfer_to(your_account, 300)
        self.assertequal(your_account.balance, 310)
        self.assertequal(self.my_account.balance, 1000000 - 300)
        self.assertrue(result)
if __name__ == 'main':
    unittest.main()
