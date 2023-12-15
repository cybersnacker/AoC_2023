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

    # A list of boxes numbered 0 to 255
    # Each box is a dictionary with lens label and focal length
    boxes = [{} for i in range(256)]
    sum_of_focusing_power = 0

    for e in entries:
        # Add lens to the correct box number in the boxes list
        if '=' in e:
            label, fl = e.split('=')
            box_num = custom_hash(label)
            boxes[box_num][label] = int(fl)
        else:
            # Remove lens from box,
            label = e[:-1]
            box_num = custom_hash(label)
            if label in boxes[box_num]:
                del boxes[box_num][label]
    
    for box_num, box in enumerate(boxes):
        for lens_num, fl in enumerate(box.values()):
            focusing_power = (1 + box_num) * (1 + lens_num) * fl
            sum_of_focusing_power += focusing_power
    
    print("Sum: ", sum_of_focusing_power)