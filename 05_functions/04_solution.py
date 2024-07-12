import math

def answer(radius):
    area = math.pi * radius ** 2 
    circumference = 2 * math.pi * radius
    return area, circumference

radius = int(input('Enter the radius of the circle: '))

my_area, my_circumference = answer(radius)
my_area = '{:.2f}'.format(my_area)
my_circumference = '{:.2f}'.format(my_circumference)
print(f'if the radius of the circle is {radius} then, area is {my_area} and circumference is {my_circumference}')