import random


def sort_one_billion_random_numbers():
    # Generate a list of one billion random numbers
    random_numbers = [random.randint(0, 1000000000) for i in range(1000000000)]

    # Sort the list of numbers
    sorted_numbers = sorted(random_numbers)

    if (sorted_numbers != None):
        return True
    else:
        return False

sort_one_billion_random_numbers()
