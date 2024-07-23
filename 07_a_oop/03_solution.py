import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass should implement this!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
circle = Circle(5)
print(circle.area())  # Output: 78.53981633974483 (approx.)

rectangle = Rectangle(4, 6)
print(rectangle.area())  # Output: 24