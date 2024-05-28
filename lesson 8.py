class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
    def stop(self):
        print('Машина остановилась')
    def change_color(self, new_color):
        self.color = new_color
gentra = Car('Ravon', 'Black', 2022) # Сначала создал экземпляр машины
gentra.change_color('White') # Решил покрасить машину в белый цвет
gentra.change_color()

