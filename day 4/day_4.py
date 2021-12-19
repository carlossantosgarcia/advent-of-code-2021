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
            break
