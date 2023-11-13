import unittest
from modules.customer import Customer
from modules.account import Account


class TestWithdrawal(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Delila', 'Delila@email.com')
        self.account = Account(100, self.customer)

    def test_withdrawal(self):
        self.account.withdrawal(50)
        self.assertEqual(self.account.balance, 50)
