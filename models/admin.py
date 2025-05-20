from models.customer import Customer

class Admin(Customer):
    def __init__(self, name, customer_id, store):
        super().__init__(name, customer_id)
        self.store = store
