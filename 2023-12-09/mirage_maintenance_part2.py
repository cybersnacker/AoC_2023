import re
import numpy as np

def parse_input(filepath):
    with open(filepath, 'r') as rf:
        entries = rf.readlines()

    processed_entries = []
    for e in entries:
        e = list(map(int, re.findall('-?\d+', e.strip())))
        processed_entries.append(e)

    return processed_entries

def get_extrapolated_value(sequence):
    first_numbers = []
    while not np.all(sequence == 0):
        first_numbers.append(sequence[0])
        sequence = np.diff(sequence)
        if np.all(sequence == 0):
            cum_diff = first_numbers[-1]
            for i in range(len(first_numbers)-1, 0, -1):
                cum_diff = first_numbers[i-1] - cum_diff
            return cum_diff
        #break

if __name__ == '__main__':
    entries = parse_input('2023-12-09/input.txt')
    sum_of_extrapolated_values = 0
    for e in entries:
        extrapolated_value = get_extrapolated_value(np.array(e))
        print(extrapolated_value)
        sum_of_extrapolated_values += extrapolated_value

    print("Sum of extrapolated values:", sum_of_extrapolated_values)