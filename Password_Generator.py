import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+<>?,./1234567890'


def generate(length) -> str:
    password = ''
    for char in range(length):
        password += random.choice(chars)
    return password


if __name__ == '__main__':
    print(generate(10))
