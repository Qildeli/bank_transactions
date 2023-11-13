from .account import Account


class SavingsAccount(Account):
    def __init__(self, account_id, balance, customer, interest_rate):
        super().__init__(self, account_id, balance, customer)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        interest = self.balance + amount * self.interest_rate
        return f"balance with interest rate is {interest}"
