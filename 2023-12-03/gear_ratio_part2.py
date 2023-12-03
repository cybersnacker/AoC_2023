import numpy as np
import itertools

with open('2023-12-03/input.txt', 'r') as rf:
    entries = rf.readlines()

#Not-symbol_list, since we don't know the exhaustive list of symbols
not_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']


# Create a 2D character array so we can slice and find neighboring characters
entries_array = [[*(e.rstrip())] for e in entries]
entries_array = np.array(entries_array)


def get_star_neighboring_pos(i, j, arr):
    """
    Given 2D position of a number, return positions of star neighbors if exists
    Return_list is a list of tuples
    """
    # max and min to handle the first and last rows/columns
    i_min = max(i-1, 0)
    i_max = min(i+2, arr.shape[0])
    j_min = max(j-1, 0)
    j_max = min(j+2, arr.shape[1])
    # If any neighbor is a star, return its position
    return_list = []

    # The positions should correspond to the entries array, this identifies a unique star
    for ii, jj in itertools.product(range(i_min, i_max), range(j_min, j_max)):
        if arr[ii, jj] == '*':
            return_list.append((ii, jj))
    return return_list


sum_of_gear_ratios = 0
gear_map = dict()
# To track contiguous numbers across lines, initialize before loop. 
# Couldn't decipher or assume from description
track_number = []
star_positions = []
symbol_neighbor = False
for i, e in enumerate(entries_array):
    for j, c in enumerate(e):
        if c.isdigit():
              # Track the number and see if there is a star in the neighborhood
              track_number.append(c)
              star_positions+= get_star_neighboring_pos(i=i, j=j, arr=entries_array)
        else:
            # Start processing the numbers when a non-number is encountered
            for pos in set(star_positions):
                if pos in gear_map:
                    gear_map[pos].append(int(''.join(track_number)))
                else:
                    gear_map[pos] = [int(''.join(track_number))]
            track_number = []
            star_positions = []

for k, v in gear_map.items():
    if len(v) == 2:
        sum_of_gear_ratios += (v[0] * v[1])

print("Sum of gear ratios is: ", sum_of_gear_ratios)