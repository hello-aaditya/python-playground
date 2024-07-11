n = int(input('Enter a number: '))

sum = 0

for element in range(0, n+1):
    if(element & 1 == 0):
        sum += element
print(f'Sum of even numbers till n is: {sum}')