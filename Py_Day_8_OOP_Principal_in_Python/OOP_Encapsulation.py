class Car:
    def __init__(self, brand, speed):
        self.brand = brand         # public
        self._speed = speed        # protected (by convention)
        self.__engine_status = "OFF"  # private (name mangling)

    def start_engine(self):
        self.__engine_status = "ON"
        print(f"{self.brand} engine started.")

    def get_engine_status(self):
        return self.__engine_status

# Using the class
my_car = Car("Toyota", 180)
my_car.start_engine()
print("Engine Status:", my_car.get_engine_status())

# Accessing private variable directly (will fail)
# print(my_car.__engine_status)  # ❌ Error
