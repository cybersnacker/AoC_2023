import re
import math
with open('2023-12-06/input.txt', 'r') as rf:
    entries = rf.readlines()

time = int(''.join(re.findall('\d+', entries[0])))
distance = int(''.join(re.findall('\d+', entries[1])))

root1 = (time + ((time ** 2 - 4*distance) ** 0.5))/(2)
root2 = (time - ((time ** 2 - 4*distance) ** 0.5))/(2)
print(math.floor(root1) - math.ceil(root2)+1)
