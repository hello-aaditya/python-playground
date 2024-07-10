order_size = input('Size of the cup: ')
extra_shot = bool(input('Want Extra Shot of Espresso (True/False): '))

if (extra_shot):
    order_size += ' size cup of Coffe with an extra shot'

else:
    order_size += ' size cup of Coffe'

print(f'order: {order_size}')

