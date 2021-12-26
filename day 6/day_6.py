import numpy as np


def read_input(file):
    """Creates an array with the initial fish"""
    lanterns = []
    for line in open(file):
        for elem in line.rstrip().split(','):
            lanterns.append(int(elem))
    return np.array(lanterns)


def count_lanterfish(file, epochs):
    """Counts the number of fish after a given number of iterations.

    Args:
        file (str): Path to input file
        epochs (int): Number of iterations to simulate
    """
    t0 = read_input(file)
    print(f'Initial state {t0}')
    for _ in range(epochs):
        t0 = t0 - np.ones(len(t0))
        new_fish = np.sum(t0 == -1)
        t0 = np.where(t0 == -1, 6, t0)
        if np.sum(new_fish) > 0:
            t0 = np.append(t0, 8*np.ones(new_fish))
    return len(t0)


if __name__ == "__main__":

    # Task 1
    print('### TASK 1 ###')
    print(
        f'Test result: {count_lanterfish("test_input.txt", epochs = 80)}')
    print(
        f'Input result: {count_lanterfish("input.txt", epochs = 80)}')
    print('\n')

    # Task 2
    print('### TASK 2 ###')
    print(
        f'Test result: {count_lanterfish("test_input.txt", epochs = 256)}')
    print(
        f'Input result: {count_lanterfish("input.txt", epochs = 256)}')