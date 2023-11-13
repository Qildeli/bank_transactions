import unittest
from modules.customer import Customer
from modules.account import Account
from modules.transaction import Transaction, process_transaction


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer('Delila', 'Delila@email.com')
        self.customer2 = Customer('Tom', 'Tom@email.com')
        self.source_account = Account(100, self.customer1)
        self.destination_account = Account(50, self.customer2)

    def test_transaction(self):
        transaction = Transaction(50, self.source_account, self.destination_account)
        process_transaction(transaction)

        self.assertEqual(self.source_account.balance, 50)
        self.assertEqual(self.destination_account.balance, 100)
