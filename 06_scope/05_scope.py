x = 99

def f1():
    x = 88
    def f2():
        print(x)
    f2()

f1()


"""
EXPLANATION OF OUTPUT:

    The global variable x is 99.
    The local variable x within f1 is 88.
    The function f2, when called, prints the x from the local scope of f1 (the nearest enclosing scope), which is 88.
"""