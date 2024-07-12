def sum_all(*args):
    return sum(args)

n = int(input('enter n number: '))
numbers = []
while n:
    my_num = int(input('Enter the number: '))
    numbers.append(my_num)
    n = n-1

result = sum_all(*numbers)
print(result)