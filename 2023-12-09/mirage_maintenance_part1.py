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
    last_numbers = []
    while not np.all(sequence == 0):
        last_numbers.append(sequence[-1])
        sequence = np.diff(sequence)
        if np.all(sequence == 0):
            return np.array(last_numbers).cumsum()[-1]

if __name__ == '__main__':
    entries = parse_input('2023-12-09/input.txt')
    sum_of_extrapolated_values = 0
    for e in entries:
        extrapolated_value = get_extrapolated_value(np.array(e))
        sum_of_extrapolated_values += extrapolated_value

    print("Sum of extrapolated values:", sum_of_extrapolated_values)