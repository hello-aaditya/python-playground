distance = int(input('Enter the distance: '))
transport = ''

if (distance < 3):
    transport = 'walk'

elif (distance > 3 and distance < 15):
    transport = 'Bike'

elif (distance > 15):
    transport = 'Car'

print(f'AI suggests choose {transport} as your transport.')