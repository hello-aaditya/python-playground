num = int(input('Enter a number: '))
isPrime = True

if num <= 1:
    isPrime = False
else:
    for i in range(2,int(num**0.5) + 1):
        if(num % i == 0):
            isPrime = False
            break

if isPrime:
    print(f'{num} is a prime number')

else:
    print(f'{num} is not a prime number')