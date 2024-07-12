x = 99
def funct3():
    global x #not a good practice
    x = 12

funct3()
print(x)

"""
When you explicitly declare a variable as global within a function, any changes you make to that variable will affect the global scope.

EXPLANATION OF OUTPUT

    The initial value of the global x is 99.
    The function funct3 changes the global x to 12 by using the global keyword.
    After the function call, the global x has the value 12.
    The print(x) statement prints 12, reflecting the change made by the function.
"""