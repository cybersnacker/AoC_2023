import numpy as np

def parse_input():
   with open('2023-12-05/input.txt', 'r') as rf:
       entries = rf.readlines()
   entries = [e.rstrip() for e in entries if e!='\n']
   return entries

def check_valid_seed(seed_list, input_num):
    for i in range(0, len(seed_list), 2):
        if seed_list[i] <= input_num < seed_list[i]+seed_list[i+1]:
            return True
    return False

def inverse_corresponding_number(mapping, input_num):
    for m in mapping:
        src, dest, rng = m
        if src <= input_num < src + rng:
            offset = input_num - src
            return dest + offset
    return input_num

def get_corresponding_number(mapping, input_num):
    for m in mapping:
        dest, src, rng = m
        if src <= input_num < src + rng:
            offset = input_num - src
            return dest + offset
    return input_num

if __name__ == '__main__':
    entries = parse_input()
    seeds = [int(s) for s in entries[0].split(': ')[1].split(' ')]
    map_dict = {}
    for e in entries[1:]:
        if 'map' in e:
            key = e.split(' ')[0]
            map_dict[key] = []
        else:
            map_dict[key].append([int(s) for s in e.split(' ')])

    interesting_locations = []
    for v in map_dict['humidity-to-location']:
        interesting_locations += [v[1], (v[1]+v[2]-1)]

    interesting_humidity = [inverse_corresponding_number(map_dict['humidity-to-location'], loc) for loc in interesting_locations]
    for v in map_dict['humidity-to-location']:
        interesting_humidity += [v[1], (v[1]+v[2]-1)]
    for v in map_dict['temperature-to-humidity']:
        interesting_humidity += [v[0], v[1]+v[2]-1]

    interesting_temperature = [inverse_corresponding_number(map_dict['temperature-to-humidity'], hum) for hum in interesting_humidity]
    for v in map_dict['temperature-to-humidity']:
        interesting_temperature += [v[1], (v[1]+v[2]-1)]
    for v in map_dict['light-to-temperature']:
        interesting_temperature += [v[0], v[1]+v[2]-1]

    interesting_light = [inverse_corresponding_number(map_dict['light-to-temperature'], temp) for temp in interesting_temperature]
    for v in map_dict['light-to-temperature']:
        interesting_light += [v[1], (v[1]+v[2]-1)]
    for v in map_dict['water-to-light']:
        interesting_light += [v[0], v[1]+v[2]-1]

    interesting_water = [inverse_corresponding_number(map_dict['water-to-light'], lit) for lit in interesting_light]
    for v in map_dict['water-to-light']:
        interesting_water += [v[1], (v[1]+v[2]-1)]
    for v in map_dict['fertilizer-to-water']:
        interesting_water += [v[0], v[1]+v[2]-1]

    interesting_fertilizer = [inverse_corresponding_number(map_dict['fertilizer-to-water'], wat) for wat in interesting_water]
    for v in map_dict['fertilizer-to-water']:
        interesting_fertilizer += [v[1], (v[1]+v[2]-1)]
    for v in map_dict['soil-to-fertilizer']:
        interesting_fertilizer += [v[0], v[1]+v[2]-1]
        
    interesting_soil = [inverse_corresponding_number(map_dict['soil-to-fertilizer'], fert) for fert in interesting_fertilizer]
    for v in map_dict['soil-to-fertilizer']:
        interesting_soil += [v[1], (v[1]+v[2]-1)]
    for v in map_dict['seed-to-soil']:
        interesting_soil += [v[0], v[1]+v[2]-1]

    candidate_seeds = [inverse_corresponding_number(map_dict['seed-to-soil'], sl) for sl in interesting_soil]
    for v in map_dict['seed-to-soil']:
        candidate_seeds += [v[1], (v[1]+v[2]-1)]

    interesting_seeds = [sd for sd in candidate_seeds if check_valid_seed(seeds, sd)]
    for i in range(0, len(seeds), 2):
        interesting_seeds += [seeds[i], seeds[i]+seeds[i+1]-1]

    interesting_seeds = set(interesting_seeds)
    # print(interesting_seeds)

    # Part 1
    locs = []
    for s in interesting_seeds:
        soil_num = get_corresponding_number(map_dict['seed-to-soil'], s)
        fertilizer_num = get_corresponding_number(map_dict['soil-to-fertilizer'], soil_num)
        water_num = get_corresponding_number(map_dict['fertilizer-to-water'], fertilizer_num)
        light_num = get_corresponding_number(map_dict['water-to-light'], water_num)
        temp_num = get_corresponding_number(map_dict['light-to-temperature'], light_num)
        hum_num = get_corresponding_number(map_dict['temperature-to-humidity'], temp_num)
        loc_num = get_corresponding_number(map_dict['humidity-to-location'], hum_num)
        # print(soil_num, fertilizer_num, water_num, light_num, temp_num, hum_num, loc_num)
        locs.append(loc_num)
    print("Closest location: ", min(locs))



    # interesting_seeds = []
    # for i in range(0, len(seeds), 2):
    #     interesting_seeds += [seeds[i], (seeds[i]+seeds[i+1]-1)]
    # #print(interesting_seeds)
        
    # for v in map_dict['seed-to-soil']:
    #     interesting_seeds += [v[1], (v[1]+v[2]-1)]
    # print(interesting_seeds)

    # interesting_soils = []
    # for v in map_dict['seed-to-soil']:
    #     interesting_soils += [v[0], (v[0]+v[2]-1)]

    # for v in map_dict['seed-to-soil']:
    #     interesting_soils += [v[1], (v[1]+v[2]-1)]

    # for soil in interesting_soils:
    #     candidate_seed = inverse_corresponding_number(map_dict['seed-to-soil'], soil)
    #     if check_valid_seed(seeds,candidate_seed):
    #         interesting_seeds.append(candidate_seed)

    # print(interesting_seeds)
    
    