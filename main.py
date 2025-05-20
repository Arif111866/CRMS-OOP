import getpass
from models.rental_store import RentalStore
from models.van import Van
from models.truck import Truck
from models.suv import SUV
from models.sedan import Sedan
from models.sports_car import SportsCar
from models.admin import Admin
from models.regular_customer import RegularCustomer

def preload_vehicles(store):
    # Add some Van 
    store.add_vehicle(Van("Toyota", "HiAce", 2021, "REG-001", 8))
    store.add_vehicle(Van("Ford", "Transit", 2022, "REG-002", 9))
    store.add_vehicle(Van("Nissan", "NV200", 2023, "REG-003", 7))

    # Add some Truck 
    store.add_vehicle(Truck("Volvo", "FH16", 2021, "REG-101", 2))
    store.add_vehicle(Truck("Scania", "R500", 2022, "REG-102", 2))
    store.add_vehicle(Truck("Mercedes", "Actros", 2023, "REG-103", 2))

    # Add some SUV 
    store.add_vehicle(SUV("Toyota", "Land Cruiser", 2021, "REG-201", 7))
    store.add_vehicle(SUV("Ford", "Explorer", 2022, "REG-202", 6))
    store.add_vehicle(SUV("Honda", "CR-V", 2023, "REG-203", 5))

    # Add some Sedan 
    store.add_vehicle(Sedan("Honda", "Civic", 2021, "REG-301", 5))
    store.add_vehicle(Sedan("Toyota", "Corolla", 2022, "REG-302", 5))
    store.add_vehicle(Sedan("Mazda", "3", 2023, "REG-303", 5))

    # Add some SportsCar 
    store.add_vehicle(SportsCar("Porsche", "911", 2021, "REG-401", 2))
    store.add_vehicle(SportsCar("Ferrari", "F8", 2022, "REG-402", 2))
    store.add_vehicle(SportsCar("Lamborghini", "Huracan", 2023, "REG-403", 2))


def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. View All Vehicles")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            reg_no = input("Enter registration number: ")
            seats = int(input("Enter number of seats: "))
            type_choice = input("Enter type (Van/Truck/SUV/Sedan/SportsCar): ").lower()

            vehicle_class = {
                "van": Van,
                "truck": Truck,
                "suv": SUV,
                "sedan": Sedan,
                "sportscar": SportsCar
            }.get(type_choice)

            if vehicle_class:
                vehicle = vehicle_class(make, model, int(year), reg_no, seats)
                admin.store.add_vehicle(vehicle)
                print("Vehicle added.")
            else:
                print("Invalid type.")
        elif choice == "2":
            reg_no = input("Enter registration number to remove: ")
            admin.store.remove_vehicle(reg_no)
            print("Vehicle removed.")
        elif choice == "3":
            admin.store.display_vehicles()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def customer_menu(customer, store):
    while True:
        print("\nCustomer Menu:")
        print("1. Rent a Vehicle")
        print("2. Return a Vehicle")
        print("3. View All Vehicles")
        print("4. View Rented Vehicles")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            reg = input("Enter registration number to rent: ")
            vehicle = store.find_vehicle(reg)
            if vehicle:
                fname = input("Enter your first name: ")
                lname = input("Enter your surname: ")
                customer.rent_vehicle(vehicle)
                print(f"{fname} {lname} rented: {vehicle.year} {vehicle.__class__.__name__} {vehicle.make} {vehicle.model} - {vehicle.registration_number} | Seats: {vehicle.seats}")
            else:
                print("Vehicle not found.")
        elif choice == "2":
            reg = input("Enter registration number to return: ")
            vehicle = store.find_vehicle(reg)
            if vehicle:
                customer.return_vehicle(vehicle)
            else:
                print("Vehicle not found.")
        elif choice == "3":
            store.display_vehicles()
        elif choice == "4":
            customer.display_rented_vehicles()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main():
    store = RentalStore()
    preload_vehicles(store)

    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter admin password: ")
            if password == "admin":
                admin = Admin("Admin", "000", store)
                admin_menu(admin)
            else:
                print("Incorrect password.")
        elif choice == "2":
            name = input("Enter your name: ")
            cid = input("Enter your customer ID: ")
            customer = RegularCustomer(name, cid)
            customer_menu(customer, store)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")
