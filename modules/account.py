import uuid
from .customer import Customer


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