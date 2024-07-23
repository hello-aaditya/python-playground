class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity
    
    def restock(self, amount):
        self.quantity += amount
    
    
product1 = Product('Laptop', 1000, 5)
print(product1.get_total_value())

product1.restock(3)
print(product1.get_total_value())