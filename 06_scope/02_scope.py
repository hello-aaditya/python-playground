username = 'mbps'

def func():
    #username = 'megabits'
    print(username)

print(username)
func()

"""
When you call func(), it tries to print the variable username.
Since username is not defined locally within the function (because it is commented out), 
Python searches for username in the enclosing scope, which is the global scope in this case. 
It finds the global variable username with the value 'mbps' and prints it.

CONCLUSION:
if a variable is not found in the local scope of a function, Python will search for it in the global scope. 
This is known as the LEGB rule in Python (Local, Enclosing, Global, Built-in). 
In this case, since username is not defined locally within func, it looks for username in the global scope and finds it.
"""