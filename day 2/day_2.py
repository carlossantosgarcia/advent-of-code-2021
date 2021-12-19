import numpy as np

def compute_horiz_depth(instructions):
    """ Computes horizontal position and depth of submarine after following instructions"""
    horiz, depth = 0,0
    for command in instructions:
        direction, value = command.split(' ')
        value = int(value)
        if direction == "forward":
            horiz += value
        elif direction == "down":
            depth += value
        else: 
            depth -= value
    return horiz, depth

def compute_horiz_depth_aim(instructions):
    """ Computes horizontal position and depth of submarine after following instructions taking aim into account"""
    horiz, depth, aim = 0,0,0
    for command in instructions:
        direction, value = command.split(' ')
        value = int(value)
        if direction == "forward":
            horiz += value
            depth += value*aim
        elif direction == "down":
            aim += value
        else: 
            aim -= value
    return horiz, depth


if __name__ == "__main__":
    # Loading the data
    test_data = [line.rstrip() for line in open("test_input.txt")]
    input_data = [line.rstrip() for line in open("input.txt")] 

    # Task 1
    test_horiz, test_depth = compute_horiz_depth(test_data)
    print(f'Test result: {test_horiz*test_depth}')
    horiz, depth = compute_horiz_depth(input_data)
    print(f'Input result: {horiz*depth}')

    # Task 2
    test_horiz, test_depth = compute_horiz_depth_aim(test_data)
    print(f'Test result: {test_horiz*test_depth}')
    horiz, depth = compute_horiz_depth_aim(input_data)
    print(f'Input result: {horiz*depth}')
