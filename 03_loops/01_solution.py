numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

countPositive = 0
for element in numbers:
    if element > 0:
        countPositive += 1
print(f'Total count of positive no is: {countPositive}')