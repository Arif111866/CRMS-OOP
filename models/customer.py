class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle):
        if vehicle.is_available():
            vehicle.set_availability(False)
            self.rented_vehicles.append(vehicle)
            print(f"{vehicle.model} rented successfully.")
        else:
            print("Vehicle not available.")

    def return_vehicle(self, vehicle):
        if vehicle in self.rented_vehicles:
            vehicle.set_availability(True)
            self.rented_vehicles.remove(vehicle)
            print(f"{vehicle.model} returned successfully.")
        else:
            print("You didn’t rent this vehicle.")

    def display_rented_vehicles(self):
        if not self.rented_vehicles:
            print("No vehicles rented.")
        for v in self.rented_vehicles:
            print(f"{v.make} {v.model} - {v.registration_number}")