class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email


class Account:
    def __init__(self, account_id, balance, customer):
        self.account_id = account_id
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawal(self, amount):
        if amount > 0:
            self.balance -= amount
        

class Transaction:
    def __init__(self, transaction_id, amount, source_account
                 ,destination_account, timestamp):
        self.transaction_id = transaction_id
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.timestamp = timestamp


class SavingsAccount(Account):
    def __init__(self, interest):
        super().__init__(self)
        self.interest = interest

    def deposit(self, amount, interest):
        self.amount = amount



def process_transaction(transaction):
    if transaction.source_account.balance >= transaction.amount:
        transaction.source_account.withdrawal(transaction.amount)
        transaction.destination_account.deposit(transaction.amount)

