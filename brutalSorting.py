import random
import time


def sort_one_billion_random_numbers():

    # start time
    start = time.time()

    # Generate a list of one billion random numbers
    random_numbers = [random.randint(0, 1000000) for i in range(100000000)]

    # Sort the list of numbers
    sorted_numbers = sorted(random_numbers)

    # end time
    end = time.time()
    print(f'Time taken: {abs(start - end)}')


if __name__ == "__main__":
    sort_one_billion_random_numbers()
