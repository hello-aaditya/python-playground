def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i;

num = int(input('Enter a number: '))
for i in even_generator(num):
    print(i)