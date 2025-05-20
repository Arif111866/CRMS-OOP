class RentalStore:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, registration_number):
        self.vehicles = [v for v in self.vehicles if v.registration_number != registration_number]

    def find_vehicle(self, registration_number):
        for v in self.vehicles:
            if v.registration_number == registration_number:
                return v
        return None

    def display_vehicles(self):
        available = [v for v in self.vehicles if v.is_available()]
        if not available:
            print("No vehicles available.")
        for v in available:
            print(f"{v.make} {v.model} - {v.registration_number}")