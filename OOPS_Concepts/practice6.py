"""Create a class Vehicle and make Car, Boat, Plane child classes of Vehicle:"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Boat is sailing")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Tooring 20")
plane1 = Plane("Boeing", "747")

for x in(car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()  # Output: Vehicle is moving Boat is sailing Plane is flying