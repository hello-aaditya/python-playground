x = 99

def f1():
    x = 88
    def f2():
        print(x)
    return f2

my_result = f1()
#print(my_result)
my_result()


"""
Q] WHY my_result IS CALLED LIKE FUNCTION (my_result(), means use a paranthesis) ?
ANSWER:
point no.1: When you call f1(), it returns the function f2. This means my_result will hold the returned function f2, not the result of executing f2.

point no.2: my_result holds a reference to the function f2, not its return value because f1() returns f2. 
            So when you call my_result(), you're essentially calling f2(), which is why it needs parentheses.
point no.3: If you print my_result, it will show you that my_result is a function.
            This output indicates that my_result is a function located at a specific memory address.


CONCLUSION:

-    my_result holds a reference to the function f2.
-    Calling my_result() actually calls f2().
-    Printing my_result shows that it is a function object.
            
"""