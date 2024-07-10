animal = input('Enter the animal species: ')
age = int(input('''Enter it's age: '''))

food = ''

if(animal == 'dog' and age < 2):
    food = 'Puppy Food'

if(animal == 'dog' and age > 2):
    food = 'Senior Dog Food'

if(animal == 'cat' and age < 5):
    food = 'Junior Cat Food'

if(animal == 'cat' and age > 5):
    food = 'Senior Cat Food'

print(food)