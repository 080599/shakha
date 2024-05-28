class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Год выпуска: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Количество дверей: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_size):
        super().__init__(brand, year)
        self.engine_size = engine_size

    def display_info(self):
        super().display_info()
        print(f"Объем двигателя: {self.engine_size} куб. см")

my_car = Car("KIA", 2022, 4)
my_motorcycle = Motorcycle("BYD", 2021, 600)

print("Информация об автомобиле:")
my_car.display_info()

print("\nИнформация о мотоцикле:")
my_motorcycle.display_info()