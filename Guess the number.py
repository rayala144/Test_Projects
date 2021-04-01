import random


def user_guess(x):
    random_number = random.randint(1, x)
    guess_value = 0
    while guess_value != random_number:
        guess_value = int(input(f"Enter a number between 1 and {x}: "))
        if (guess_value > x):
            print(f"Stick with the range (1 to {x}) please!!!")
        elif(guess_value < 0):
            print(f"Stick with the range (1 to {x}) please!!!")
        if (guess_value < random_number and guess_value > 0):
            print(f"Sorry, your guessing number {guess_value} is too low!")
        elif (guess_value > random_number and guess_value < x):
            print(f"Sorry, your guessing number {guess_value} is too high!")

    print(
        f"Yay! Congrats. You have guessed the number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    message = ''
    while message != 'c':
        if low != high:
            guess_value = random.randint(low, high)
        else:
            guess_value = low #could be high also because low = high
        message = input(f"Is my guess ({guess_value}) too low(L) or too high(H) or correct(C)?? ")
        if message == 'h'.lower():
            high = guess_value - 1
        elif message == 'l'.lower():
            low = guess_value + 1
    print(f"Yay! I got the number {guess_value} correctly!!")


guess_range = int(input("What's the range you want me to guess over? "))
computer_guess(guess_range)
