class My_car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f'{self.brand} {self.model}'

car1 = My_car("Toyota", "Corolla")
print(car1.display())

car2 = My_car('Tata', 'Safari')
print(car2.display())