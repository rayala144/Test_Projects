import random

print("Welcome to password generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+<>?,./1234567890'

number = int(input('Enter the no. of passwords you want to generate: '))

if number > 0:
    length = int(input('Enter the length of your password: '))

if number == 1:
    print('\nHere is your password:')
elif number <= 0:
    print('Enter a valid number!!!!')
else:
    print('\nHere are your passwords:')

for pwd in range(number):
    password = ''
    for char in range(length):
        password += random.choice(chars)
    print(password)
