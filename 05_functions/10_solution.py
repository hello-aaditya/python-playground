def factorial(num):
    # base case
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input('Enter a number: '))
answer = factorial(num)
print(answer)