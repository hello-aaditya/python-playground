
file = open('yotube.txt', 'w')

try:
    file.write('coding with coffee')
finally:
    file.close()


"""
#second way:


with open('youtube.txt', 'w') as file:
    file.write('python with coffee')

    """