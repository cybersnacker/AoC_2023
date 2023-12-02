from collections import Counter
import re

with open('input.txt', 'r') as rf:
    entries = rf.readlines()
    
sum_of_power_of_sets = 0
for e in entries:
    max_r_cubes = 0
    max_g_cubes = 0
    max_b_cubes = 0

    # Create subsets
    game_id, sets = e.split(':')
    id_num = int(game_id.split(' ')[-1])
    subsets = sets.split(';')
    subsets[-1] = subsets[-1].rstrip()
    
    for s in subsets:
        # possible_flag = True
        # Get numeric part of the string and convert to in
        num = re.findall(r'\d+', s)
        num = list(map(int, num))
        # Get color part of the string
        color = re.findall(r'[a-zA-Z]+', s)
        # Create dictionary in the form {'red': 1, 'blue: 2, 'green': 3}
        subset_color_count = dict(zip(color, num))
        max_r_cubes = max(subset_color_count.get('red', 0), max_r_cubes)
        max_b_cubes = max(subset_color_count.get('blue', 0), max_b_cubes)
        max_g_cubes = max(subset_color_count.get('green', 0), max_g_cubes)
    
    sum_of_power_of_sets+= (max_r_cubes*max_b_cubes*max_g_cubes)

print(sum_of_power_of_sets)