import re
with open('2023-12-04/input.txt') as rf:
    entries = rf.readlines()

entries = [e.rstrip() for e in entries]

sum_of_points = 0
for e in entries:
    card_id, lst = e.split(':')
    winning, actual = lst.split('|')
    winning = re.findall(r'\d+', winning)
    actual = re.findall(r'\d+', actual)
    if len(set(winning) & set(actual)) > 0:
        card_points = 1 * (2 ** (len(set(winning) & set(actual)) - 1))
    else:
        card_points = 0
    sum_of_points += card_points

print("Sum of points: ", sum_of_points)