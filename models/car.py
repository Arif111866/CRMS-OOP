from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, registration_number, seats, availability=True):
        super().__init__(make, model, year, registration_number, availability)
        self.seats = seats