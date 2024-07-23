class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}"
    
    def give_raise(self, amount):
        self.salary += amount


employee = Employee('John Doe', 'E123', 50000)
print(employee.get_details()) 

employee.give_raise(5000)
print(employee.get_details())