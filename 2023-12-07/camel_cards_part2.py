from collections import Counter
import functools

def parse_input(filepath):
    with open(filepath, 'r') as rf:
        entries = rf.readlines()

    entries_map = {}
    for e in entries:
        hand, entries_map[hand] = e.rstrip().split(' ')

    return entries_map

def camel_sort(h1, h2):
    camel_map = {
        'J' : 1,
        '2' : 2, 
        '3' : 3,
        '4' : 4, 
        '5' : 5, 
        '6' : 6,
        '7' : 7, 
        '8' : 8,
        '9' : 9, 
        'T' : 10, 
        'Q' : 12,
        'K' : 13, 
        'A' : 14}
    for i in range(5):
        if camel_map[h1[i]] > camel_map[h2[i]]:
            return -1
        elif camel_map[h1[i]] < camel_map[h2[i]]:
            return 1
        else:
            continue
        

def categorize_hands(hand, hand_type_map):
    counts = Counter(hand)
    # Find new category if there is a J
    if 'J' in counts.keys():
        count_val = counts.values()
        if len(count_val) == 2 or len(count_val) == 1:
            hand_type_map['5OK'].append(hand)
        elif sorted(count_val) == [1,2,2]:
            if counts['J'] == 2:
                hand_type_map['4OK'].append(hand)
            else:
                hand_type_map['FH'].append(hand)
        elif sorted(count_val) == [1,1,3]:
            hand_type_map['4OK'].append(hand)
        elif sorted(count_val) == [1,1,1,2]:
            hand_type_map['3OK'].append(hand)
        elif len(count_val) == 5:
            hand_type_map['1P'].append(hand)
        else:
            hand_type_map['2P'].append(hand)
    else:
    # No change if there is no J
        count_val = counts.values()
        if set(count_val) == set([5]):
            hand_type_map['5OK'].append(hand)
        elif set(count_val) == set([4, 1]):
            hand_type_map['4OK'].append(hand)
        elif set(count_val) == set([3, 2]):
            hand_type_map['FH'].append(hand)
        elif set(count_val) == set([3, 1]):
            hand_type_map['3OK'].append(hand)
        elif sorted(count_val) == [1,2,2]:
            hand_type_map['2P'].append(hand)
        elif 2 in set(count_val):
            hand_type_map['1P'].append(hand)
        else:
            hand_type_map['HC'].append(hand)
    

if __name__ == '__main__':
    entries_map = parse_input('2023-12-07/input.txt')

    hand_type_map = {
        "HC": [],
        "1P": [],
        "2P": [],
        "3OK": [],
        "FH": [],
        "4OK": [],
        "5OK": []
    }
    for h in entries_map.keys():
        categorize_hands(h, hand_type_map)

    for k, v in hand_type_map.items():
        hand_type_map[k] = sorted(v, key=functools.cmp_to_key(camel_sort), reverse=True)

    print(hand_type_map)
    winnings = 0
    lol = []
    for v in hand_type_map.values():
        for i in v:
            lol.append(i)

    # print(hand_type_map['HC'])
    
    print(lol)
    for multiplier, hand in enumerate(lol, start=1):
        winnings += int(entries_map[hand]) * multiplier

    print(winnings)
        