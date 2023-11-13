import unittest
from modules import Customer
from modules import Account


class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Delila', 'Delila@email.com')
        self.account = Account(100, self.customer)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
