def parse_input(filepath):
    with open(filepath, 'r') as rf:
        entries = rf.read().strip().split(',')
    return entries

def custom_hash(s):
    cur_val = 0
    for c in s:
        cur_val = ((cur_val+ord(c))*17) % 256
    return cur_val

if __name__ == '__main__':
    entries = parse_input('2023-12-15/input.txt')
    sum_custom_hash = 0
    for e in entries:
        sum_custom_hash += custom_hash(e)

    print("Sum: ", sum_custom_hash)