from bank_account import BankAccount


import unittest


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount("Ivo", 100, "$")

    def test_init(self):
        self.assertEqual(self.my_account.name, "Ivo")

    def test_str(self):
        needed_result = "Bank account for Ivo with balance of 100$"
        self.assertEqual(str(self.my_account), needed_result)

    def test_deposite(self):
        self.my_account.deposit(100)
        self.assertEqual(self.my_account.balance, 200)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)

    def test_balance(self):
        self.assertEqual(self.my_account.balance, 100)

    def test_transfer_to(self):
        your_account = BankAccount("rado", 10, "&")
        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_account, 200)
        self.assertEqual(self.my_account.balance, 100)
        self.assertEqual(your_account.balance, 10)

    def transfer_more_money_than_we_have(self):
        your_account = BankAccount("rado", 10, "&")
        self.assertFalse(your_account.trasfer_to(self.my_account, 300))
        self.assertEqual(self.my_account.balance, 1000000)
        self.assertEqual(your_account.balance, 10)

    def test_withdraw(self):

if __name__ == '__main__':
    unittest.main()
