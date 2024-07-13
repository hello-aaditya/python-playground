class My_class_car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f'{self.brand} {self.model} {self.battery_size}'

class Electric_car(My_class_car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = Electric_car('Tesla', 'Model S', '85kwh')
print(my_tesla.display())