fruit = 'Banana'

print('''choose the color of the fruit.
      type-1: for 'Green'
      type-2: for 'Yellow'
      type-3: for 'Brown' ''')

type = int(input())

if(type <= 0 or type > 3):
    print('please type the number from 1 to 3!')
    exit()


if(type == 1):
    print('Unripe')
elif(type == 2):
    print('Ripe')
else:
    print('Overripe')
