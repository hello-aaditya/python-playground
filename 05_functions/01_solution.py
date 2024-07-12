# way-1
""" 
def square_of_a_num(number):
    print(number ** 2)

num = int(input('Enter a number: '))
answer = square_of_a_num(num)
print(answer)
"""

"""
 When you call square_of_a_num(num), the function prints the square of the number directly but doesn't return any value. 
 Therefore, the answer variable is assigned None, which is why print(answer) outputs None.
"""

# way-2:

def square_of_a_num(number):
    return number ** 2

num = int(input('Enter a number: '))
answer = square_of_a_num(num)
print(answer)