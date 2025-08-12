class Car:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} created.")

    def __del__(self):
        print(f"{self.brand} destroyed.")

car1 = Car("Suzuki")
del car1  # Forces destructor
