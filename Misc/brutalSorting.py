import random
import time
import numpy as np


def sort_random_numbers(number_range, strength) -> None:

    print("Process started")

    # start time
    start = time.time()

    # Generate a list of random numbers
    random_numbers = np.array([random.randint(0, number_range) for _ in range(strength)])

    # Sort the list of numbers
    random_numbers = sorted(random_numbers)

    # end time
    end = time.time()
    print("Process ended")
    print(f'Time taken: {abs(start - end)}')


if __name__ == "__main__":
    sort_random_numbers(10000, 3400000)
