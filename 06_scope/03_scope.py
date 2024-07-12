x = 99

def func2(y):
    z = x+y
    return z

result = func2(1)
print(result)

"""
EXPLANATION OF OUTPUT:
- The global variable x has the value 99.
- When func2(1) is called, it uses the global x because x is not defined locally within the function.
- The calculation inside the function is z = 99 + 1, so z is 100.
- The function returns 100, which is assigned to result.
- The print(result) statement prints 100.
"""