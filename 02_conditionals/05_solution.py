weather = input('Enter current Weather: ')
activity = ''

if(weather == 'Sunny'):
    activity +=  'Go for a walk'

elif (weather == 'Rainy'):
    activity +=  'Read a book'

elif (weather == 'Snowy'):
    activity += 'Build a snowman'

else:
    print('Please Enter the weather again!')

print(activity)