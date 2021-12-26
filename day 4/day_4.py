import numpy as np

# Bingo grids size for this problem
# Assumed to be a square
SIDE = 5
SIZE = (SIDE, SIDE)


def read_input_puzzle(file):
    """Retrieves bingo order and grids to play with.

    Args:
        file (str): Path to file to retrieve information from

    Returns:
        tuple: list of bingo integers and list of ndarrays used as bingo grids
    """
    # Reads first line of file to get bingo order
    with open(file) as f:
        bingo_order = [int(n) for n in f.readline().strip().split(',')]

    # Reads all information from file
    with open(file) as f:
        bingo_grids = f.read().split("\n")

    # Number of grids
    nb_grids = bingo_grids.count("")

    # List of arrays
    list_grids = []
    for mat in range(nb_grids):
        list_grids.append(np.zeros(SIZE))
        for idx in range(SIDE):
            # We skip the two first lines (bingo_order and empty string)
            curr_row = [n for n in bingo_grids[6 *
                                               mat + idx + 2].split(' ') if n != ""]

            assert len(curr_row) == SIDE
            list_grids[mat][idx, :] = np.array(curr_row)
    return bingo_order, list_grids, nb_grids


def check_winner(grid):
    """Checks wether a grid has already won or not

    Args:
        grid (ndarray): 2D boolean Bingo grid

    Returns:
        bool: Returns whether grid has won.
    """
    for i in range(5):
        if np.sum(grid[i, :]) == 5 or np.sum(grid[:, i]) == 5:
            return True
    else:
        return False


def find_winner_grid(bingo_order, list_grids, nb_grids):
    """Finds winning board among list of grids with the given bingo_order list of integers chosen

    Args:
        bingo_order (list): List of chosen integers for bingo
        list_grids (list): List of 2D ndarrays representing bingo boards
        nb_grids (int): Number of bingo boards playing

    Returns:
        tuple: Returns index of winning board, list of boolean grids, list of bingo boards and integer that allowed victory
    """
    list_of_boolgrids = [np.zeros(SIZE, dtype=bool) for n in range(nb_grids)]
    for integer in bingo_order:
        winner_grids = []
        for i, grid in enumerate(list_grids):
            if integer in grid:
                coords = np.where(grid == integer)
                assert len(coords) == 2
                row, col = coords
                list_of_boolgrids[i][row, col] = True

        for j, grid in enumerate(list_of_boolgrids):
            is_winner = check_winner(grid)
            if is_winner:
                winner_grids.append(j)
        if len(winner_grids) > 0:
            return winner_grids[0], list_of_boolgrids, list_grids, integer


def compute_unmarked_sum(idx, list_of_boolgrids, list_grids, integer):
    """Computes the score of the winning board as explained in the puzzle. Returns final result

    Args:
        idx (int): Index of winning grid in the given lists
        list_of_boolgrids (list): List of boolean boards after winning
        list_grids (list): List of bingo boards

    Returns:
        int: Sum of unmarked numbers on winning board times the integer which allowed victory
    """
    return int(np.sum(np.bitwise_not(list_of_boolgrids[idx])*list_grids[idx]))*integer


def find_last_winner_grid(bingo_order, list_grids, nb_grids):
    """Finds last winning board among list of grids with the given bingo_order list of integers chosen

    Args:
        bingo_order (list): List of chosen integers for bingo
        list_grids (list): List of 2D ndarrays representing bingo boards
        nb_grids (int): Number of bingo boards playing

    Returns:
        tuple: Returns boolean and normal grids for last winner, as well as the integer that won 
    """
    list_of_boolgrids = [np.zeros(SIZE, dtype=bool) for n in range(nb_grids)]
    for integer in bingo_order:
        winner_grids = []
        for i, grid in enumerate(list_grids):
            if integer in grid:
                coords = np.where(grid == integer)
                assert len(coords) == 2
                row, col = coords
                list_of_boolgrids[i][row, col] = True

        for j, grid in enumerate(list_of_boolgrids):
            is_winner = check_winner(grid)
            if is_winner:
                winner_grids.append(j)
        if len(winner_grids) == nb_grids - 1:
            # All but one grids have already won
            last_idx = [idx for idx in range(
                nb_grids) if idx not in winner_grids][0]
            last_grid = list_grids[last_idx]
            last_bool_grid = list_of_boolgrids[last_idx]
            stop_idx = bingo_order.index(integer)

            # Last board still needs to win
            for i in range(stop_idx+1, len(bingo_order)):
                if bingo_order[i] in last_grid:
                    coords = np.where(last_grid == bingo_order[i])
                    assert len(coords) == 2
                    row, col = coords
                    last_bool_grid[row, col] = True
                if check_winner(last_bool_grid):
                    break

            return 0, [last_bool_grid], [last_grid], bingo_order[i]


if __name__ == "__main__":
    # Loading the data
    test_order, test_grids, test_nb_grids = read_input_puzzle("test_input.txt")
    order, grids, nb_grids = read_input_puzzle("input.txt")

    # Task 1
    print('### TASK 1 ###')
    print(
        f'Test result: {compute_unmarked_sum(*find_winner_grid(test_order, test_grids, test_nb_grids))}')
    print(
        f'Input result: {compute_unmarked_sum(*find_winner_grid(order, grids, nb_grids))}')
    print('\n')

    # Task 2
    print('### TASK 2 ###')
    print(
        f'Test result: {compute_unmarked_sum(*find_last_winner_grid(test_order, test_grids, test_nb_grids))}')
    print(
        f'Input result: {compute_unmarked_sum(*find_last_winner_grid(order, grids, nb_grids))}')
