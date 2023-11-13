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
            print(f'balance raised to {self.balance}')
        print('No change')

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            raise ValueError('Not enough amount')
        self.balance -= amount
        print(f'balance decreased to {self.balance}')


class SavingsAccount(Account):
    def __init__(self, account_id, balance, customer, interest_rate):
        super().__init__(self, account_id, balance, customer)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        interest = self.balance + amount * self.interest_rate
        return f"balance with interest rate is {interest}"
