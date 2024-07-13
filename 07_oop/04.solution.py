class My_class_car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f'{self.__brand}!'
    
    def display(self):
        return f'{self.__brand} {self.model} {self.battery_size}'

class Electric_car(My_class_car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = Electric_car('Tesla', 'Model S', '85kwh')

print(my_tesla.get_brand())