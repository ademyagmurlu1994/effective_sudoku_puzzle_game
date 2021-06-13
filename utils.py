import numpy as np
import random as rnd

def create_random_array(size, range=(0, 8)):
    rnd_array = []
    index = 0
    while index != size:
        rnd_number = rnd.randint(range[0], range[1])
        if rnd_number not in rnd_array:
            rnd_array.append(rnd_number)
            index += 1
    return rnd_array


def create_random_matrix():
    arr = np.arange(1, 10).astype("int")
    np.random.shuffle(arr)
    matrix = arr.reshape((3, 3))

    return matrix

