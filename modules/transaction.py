import uuid
import datetime


class Transaction:
    def __init__(self, amount, source_account
                 , destination_account):
        self.transaction_id = uuid.uuid4()
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.timestamp = datetime.datetime
