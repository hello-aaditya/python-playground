class My_class_car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f'{self.__brand}!'
    
    def display(self):
        return f'{self.__brand} {self.model} {self.battery_size}'
    
    def fuel_type(self):
        return 'Petrol or Diesel'

class Electric_car(My_class_car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return 'Electric Charge'


my_tesla = Electric_car('Tesla', 'Model S', '85kwh')

print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = My_class_car('Tata', 'Safari')
print(safari.fuel_type())