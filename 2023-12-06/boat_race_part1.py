import re
import math
with open('2023-12-06/input.txt', 'r') as rf:
    entries = rf.readlines()

times = list(map(int, re.findall('\d+', entries[0])))
distances = list(map(int, re.findall('\d+', entries[1])))
race_results = dict(zip(times, distances))

win_ways = []
for t, d in race_results.items():
    num_win_ways = 0
    for i in range(1, t-1):
        if (t - i)*i > d:
            num_win_ways += 1
    win_ways.append(num_win_ways)
win_margin = math.prod(win_ways)

print("Win margin is: ", win_margin)