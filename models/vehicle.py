class Vehicle:
    def __init__(self, make, model, year, registration_number, availability=True):
        self.make = make
        self.model = model
        self.year = year
        self.registration_number = registration_number
        self.availability = availability

    def is_available(self):
        return self.availability

    def set_availability(self, status):
        self.availability = status