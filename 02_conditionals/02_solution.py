age = int(input('Enter your age: '))
day = input('Enter the day of the week: ')

if(age >= 18):
    ticket_price = 12
    if(day == 'wednesday'):
        ticket_price -= 2
        print(f'Your ticket price is : {ticket_price}.')
    else:
        print(f'Your ticket price is : {ticket_price}.')
else:
    ticket_price = 8
    if(day == 'wednesday'):
        ticket_price -= 2
        print(f'Your ticket price is : {ticket_price}.')
    else:
        print(f'Your ticket price is : {ticket_price}.')   