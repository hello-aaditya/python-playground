password = input('Enter your password: ')
size = len(password)
protection = ''

if(size < 6):
    strength = 'Weak'

elif(size >= 6 and size <= 10):
    strength = 'Medium'

else:
    strength = 'Strong'

print(strength)