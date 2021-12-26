import numpy as np
import time

def create_diagram_from_input(file, part=1):
    """Creates an array from the input file where each element counts the number of vent lines.
    Args:
        file (str): Path to the input file.
        part (int, optional): In part 1 of the problem, we ignore diagonals. Defaults to 1.

    Returns:
        np.ndarray: Diagram array
    """

    vents_coords = [line.rstrip().split(' -> ') for line in open(file)]
    max_x = max([int(x[0].split(',')[1]) for x in vents_coords ])
    max_y = max([int(y[1].split(',')[1]) for y in vents_coords ])
    SHAPE = max(max_x+1, max_y+1)

    diagram = np.zeros((SHAPE, SHAPE))
    for coords in vents_coords:
        x1,y1 = coords[0].split(',')
        x2,y2 = coords[1].split(',')
        x1, y1, x2, y2= int(x1), int(y1), int(x2), int(y2)

        if x1 == x2:
            if y1 < y2:
                diagram[x1,y1:y2+1] += 1
            else:
                diagram[x1,y2:y1+1] += 1
        
        elif y1 == y2:
            if x1 < x2:
                diagram[x1:x2+1,y1] += 1
            else:
                diagram[x2:x1+1,y1] += 1
        
        else:
            # Diagonal lines
            if part == 1:
                continue
            else:
                # We take into account diagonals
                xstep = 1 if x1 < x2 else -1
                ystep = 1 if y1 < y2 else -1
                curr_x, curr_y = x1, y1
                diagram[curr_x, curr_y] += 1
                while (curr_x, curr_y) != (x2, y2):
                    curr_x, curr_y = curr_x + xstep, curr_y + ystep
                    diagram[curr_x, curr_y] += 1
    return diagram

def count_overlaps(diagram):
    """Returns answer"""
    return np.sum(diagram > 1)

if __name__ == "__main__":

    # Task 1
    print('### TASK 1 ###')
    print(
        f'Test result: {count_overlaps(create_diagram_from_input("test_input.txt"))}')
    print(
        f'Input result: {count_overlaps(create_diagram_from_input("input.txt"))}')
    print('\n')

    # Task 2
    print('### TASK 2 ###')
    print(
        f'Test result: {count_overlaps(create_diagram_from_input("test_input.txt", part=2))}')
    print(
        f'Input result: {count_overlaps(create_diagram_from_input("input.txt", part=2))}')