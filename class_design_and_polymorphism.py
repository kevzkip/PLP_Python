#kevin classes and polymorphism assignment
# Part 1: Smartphone Class with Encapsulation

class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.__brand = brand
        self.__model = model
        self.__battery_level = battery_level  # Encapsulated attribute

    # Method to display smartphone details
    def get_details(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Battery Level: {self.__battery_level}%"

    # Method to charge the phone
    def charge(self, amount):
        if 0 < amount <= 100 - self.__battery_level:
            self.__battery_level += amount
            print(f"Charging... Battery level is now {self.__battery_level}%")
        else:
            print("Invalid charge amount or battery full.")

# Creating a Smartphone object
print("Smartphone Details and Charging Example:")
phone = Smartphone("Apple", "iPhone 14", 50)
print(phone.get_details())
phone.charge(30)
print(phone.get_details())
print("\n" + "-"*50 + "\n")

# Part 2: Vehicle Class with Polymorphism

class Vehicle:
    def move(self):
        pass  # Empty move method, to be defined in subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Creating objects of the classes
print("Vehicle Movement Examples:")
car = Car()
plane = Plane()
boat = Boat()

# Calling move() on each object (Polymorphism)
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()
