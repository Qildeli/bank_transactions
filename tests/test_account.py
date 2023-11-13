import unittest
from modules.customer import Customer
from modules.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Delila', 'Delila@email.com')
        self.account = Account(100, self.customer)

    def test_account(self):
        self.assertEqual(self.account.balance, 100)
