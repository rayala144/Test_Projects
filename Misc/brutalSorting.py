import random
import time
import numpy as np


def sort_one_billion_random_numbers():

    print("Process started")

    # start time
    start = time.time()

    # Generate a list of one billion random numbers
    random_numbers = np.array([random.randint(0, 1000000) for i in range(10000000)])

    # Sort the list of numbers
    sorted(random_numbers)

    # end time
    end = time.time()
    print("Process ended")
    print(f'Time taken: {abs(start - end)}')


if __name__ == "__main__":
    sort_one_billion_random_numbers()
    
