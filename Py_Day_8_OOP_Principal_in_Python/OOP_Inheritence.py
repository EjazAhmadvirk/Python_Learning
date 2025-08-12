class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is moving.")

class Car(Vehicle):  # Inheriting Vehicle
    def honk(self):
        print(f"{self.brand} says: Beep beep!")

my_car = Car("Honda")
my_car.drive()
my_car.honk()
