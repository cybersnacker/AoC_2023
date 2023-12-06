def parse_input():
   with open('2023-12-05/input.txt', 'r') as rf:
       entries = rf.readlines()
   entries = [e.rstrip() for e in entries if e!='\n']
   return entries

def get_corresponding_number(mapping, input_num):
    for m in mapping:
        dest, src, rng = m
        if src <= input_num <= src + rng:
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
    
    print(map_dict)
    locs = []
    for s in seeds:
        soil_num = get_corresponding_number(map_dict['seed-to-soil'], s)
        fertilizer_num = get_corresponding_number(map_dict['soil-to-fertilizer'], soil_num)
        water_num = get_corresponding_number(map_dict['fertilizer-to-water'], fertilizer_num)
        light_num = get_corresponding_number(map_dict['water-to-light'], water_num)
        temp_num = get_corresponding_number(map_dict['light-to-temperature'], light_num)
        hum_num = get_corresponding_number(map_dict['temperature-to-humidity'], temp_num)
        loc_num = get_corresponding_number(map_dict['humidity-to-location'], hum_num)
        print(soil_num, fertilizer_num, water_num, light_num, temp_num, hum_num, loc_num)
        locs.append(loc_num)
    print("Closest location: ", min(locs))