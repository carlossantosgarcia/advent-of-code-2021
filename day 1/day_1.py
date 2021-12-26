import numpy as np


def count_nb_increases(array):
    """Counts the number of increasing values in array"""
    counter = 0
    for i in range(1, len(array)):
        counter += int(array[i] > array[i-1])
    return counter


def count_increases_sliding_window(array):
    slided_array = [array[i]+array[i+1]+array[i+2]
                    for i in range(0, len(array)-2)]
    return count_nb_increases(slided_array)


if __name__ == "__main__":
    # Loading the data
    test_data = np.loadtxt("test_input.txt")
    input_data = np.loadtxt("input.txt")

    # Task 1
    print('### TASK 1 ###')
    print(f'Test result: {count_nb_increases(test_data)}')
    print(f'Input result: {count_nb_increases(input_data)}')
    print('\n')

    # Task 2
    print('### TASK 2 ###')
    print(f'Test result: {count_increases_sliding_window(test_data)}')
    print(f'Input result: {count_increases_sliding_window(input_data)}')
