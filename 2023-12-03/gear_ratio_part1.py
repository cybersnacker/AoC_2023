import numpy as np

with open('2023-12-03/input.txt', 'r') as rf:
    entries = rf.readlines()

#Not-symbol_list, since we don't know the exhaustive list of symbols
not_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
# symbol_list = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '='
#                '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '?', '/']


# Create a 2D character array so we can slice and find neighboring characters
entries_array = [[*(e.rstrip())] for e in entries]
entries_array = np.array(entries_array)


def has_neighboring_symbol(i, j, arr):
    """
    Given 2D position of a character, return if there is a neighboring symbol in the subarray
    """
    # max and min to handle the first and last rows/columns
    i_min = max(i-1, 0)
    i_max = min(i+2, arr.shape[0])
    j_min = max(j-1, 0)
    j_max = min(j+2, arr.shape[1])
    subarr = arr[i_min: i_max, j_min: j_max]
    # If every neighbor is a digit or period, then the character doesn't have a neighboring symbol
    return ~np.isin(subarr, not_symbols).all()


sum_of_part_nums = 0
# To track contiguous numbers across lines, initialize before loop. 
# Couldn't decipher or assume from description
track_number = []
symbol_neighbor = False
for i, e in enumerate(entries_array):
    for j, c in enumerate(e):
        if c.isdigit():
          track_number.append(c)
          symbol_neighbor |= has_neighboring_symbol(i=i, j=j,arr=entries_array)
        else:
            if symbol_neighbor:
                sum_of_part_nums += int(''.join(track_number))
            # Reset to track new number and neighbor
            track_number = []
            symbol_neighbor = False

print("Sum of part numbers is: ", sum_of_part_nums)