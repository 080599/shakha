class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")

# Создание объектов Person
person1 = Person("Shakhzoda", 25)
person2 = Person("Shokhrukh", 27)
person3 = Person("Alisher", 18)

# Вывод информации о каждом объекте
print("Информация о людях:")
person1.display_info()
print("-" * 20)
person2.display_info()
print("-" * 20)
person3.display_info()