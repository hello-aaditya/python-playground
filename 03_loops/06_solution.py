my_num = int(input('Enter a number: '))
num = my_num
ans = 1

while(num):
    ans *= num
    num -= 1
print(f'Factorial of {my_num} is: {ans}')