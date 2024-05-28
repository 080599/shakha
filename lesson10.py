class Animal:
    def make_sound(self):
        print("Звук животного")

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

class Cow(Animal):
    def make_sound(self):
        print("Муу!")

# Создание объектов
dog = Dog()
cat = Cat()
cow = Cow()

# Вызов методов make_sound()
print("Собака:")
dog.make_sound()

print("Кошка:")
cat.make_sound()

print("Корова:")
cow.make_sound()