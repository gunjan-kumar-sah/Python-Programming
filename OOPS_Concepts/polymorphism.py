class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Fly!")

car1 = Car("Toyata", "Corolla", 2020)
boat1 = Boat("Yamaha", "242x", 2021)
plane1 = Plane("Boeing", "737", 2022)

for x in (car1, boat1, plane1):
    x.move()  # Output: Drive! Sail! Fly!