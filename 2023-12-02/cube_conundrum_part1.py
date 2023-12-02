from collections import Counter
import re

with open('input.txt', 'r') as rf:
    entries = rf.readlines()
    
possible = 0
for e in entries:
    max_r_cubes = 12
    max_g_cubes = 13
    max_b_cubes = 14

    # Create subsets
    game_id, sets = e.split(':')
    id_num = int(game_id.split(' ')[-1])
    subsets = sets.split(';')
    subsets[-1] = subsets[-1].rstrip()
    
    for s in subsets:
        possible_flag = True
        # Get numeric part of the string and convert to in
        num = re.findall(r'\d+', s)
        num = list(map(int, num))
        # Get color part of the string
        color = re.findall(r'[a-zA-Z]+', s)
        # Create dictionary in the form {'red': 1, 'blue: 2, 'green': 3}
        subset_color_count = dict(zip(color, num))
        #If any of the colors in the subset exceed the max number of that color, game is impossible, don't need to parse other subsets in that game
        if subset_color_count.get('red', 0) > max_r_cubes or subset_color_count.get('blue', 0) > max_b_cubes or subset_color_count.get('green', 0) > max_g_cubes:
            possible_flag = False
            break
        else:
            possible_flag = True

    if possible_flag:
        possible+= id_num
    print(id_num, "Possible value: ", possible)
            
print("Possible: ", possible)        
    