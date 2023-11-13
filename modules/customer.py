import uuid


class Customer:
    def __init__(self, name, email):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.email = email
