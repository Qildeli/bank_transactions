import datetime
import uuid

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.email = email


class Account:
    def __init__(self, account_id, balance, customer):
        self.account_id = uuid.uuid4()
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return f"balance raised to {self.balance}"

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return f"balance decreased to {self.balance}"


class Transaction:
    def __init__(self, transaction_id, amount, source_account
                 ,destination_account, timestamp):
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
    def test_deposit(self):
        deposit_1 = Account(balance=20, customer=1)
        self.assertEquals(deposit_1.deposit(), f"balance raised to {self.balance}")

