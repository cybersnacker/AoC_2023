import numpy as np
from itertools import combinations

def parse_input(filepath):
    with open(filepath, 'r') as rf:
        lines = rf.readlines()
    entries = [[w for w in line if w!='\n'] for line in lines]
    return np.array(entries)

def compute_manhattan_distance(p1, p2):
    return sum([abs(p1[0] - p2[0]), abs(p1[1] - p2[1])])

def get_expansion_offsets(point, x_arr, y_arr) -> tuple: 
     """
     Returns location after expansion
     """
     point_x, point_y = point
     expansions_x = (x_arr < point_x).sum() * 999999
     expansions_y = (y_arr < point_y).sum() * 999999
     return (point_x+expansions_x, point_y+expansions_y)

if __name__ == '__main__':
    entries = parse_input('2023-12-11/input.txt')
    no_galaxies_x = np.argwhere(np.all(entries == '.', axis=1))
    no_galaxies_y = np.argwhere(np.all(entries == '.', axis=0))
    sum_of_shortest_paths = 0
    galaxy_loc = np.argwhere(entries == '#')
   
    for num, item in enumerate(combinations(galaxy_loc, 2)):
        #print(num+1, item)
        new_p1 = get_expansion_offsets(item[0], no_galaxies_x, no_galaxies_y)
        new_p2 = get_expansion_offsets(item[1], no_galaxies_x, no_galaxies_y)
        sum_of_shortest_paths += compute_manhattan_distance(p1=new_p1, p2=new_p2)

    print(f"Sum of shortest paths {sum_of_shortest_paths}")
