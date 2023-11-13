import datetime
import uuid


class Customer:
    def __init__(self, name, email):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.email = email


class Account:
    def __init__(self, balance, customer: Customer):
        self.account_id = uuid.uuid4()
        self._balance = balance
        self.customer = customer

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return f"balance raised to {self.balance}"

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            raise ValueError('Not enough amount')
        self.balance -= amount
        return f"balance decreased to {self.balance}"


class Transaction:
    def __init__(self, amount, source_account
                 , destination_account):
        self.transaction_id = uuid.uuid4()
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.timestamp = datetime.datetime


class SavingsAccount(Account):
    def __init__(self, account_id, balance, customer, interest_rate):
        super().__init__(self, account_id, balance, customer)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        interest = self.balance + amount * self.interest_rate
        return f"balance with interest rate is {interest}"


def process_transaction(transaction: Transaction):
    if transaction.source_account.balance >= transaction.amount:
        transaction.source_account.withdrawal(transaction.amount)
        transaction.destination_account.deposit(transaction.amount)




import unittest


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Delila', 'Delila@email.com')
        self.account = Account(100, self.customer)

    def test_account(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 'balance raised to 150')

    def test_withdrawal(self):
        self.assertEqual(self.account.withdrawal(50), 'balance decreased to 50')


if __name__ == '__main__':
    unittest.main()
