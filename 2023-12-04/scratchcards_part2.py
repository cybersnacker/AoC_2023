import re
with open('2023-12-04/input.txt') as rf:
    entries = rf.readlines()

entries = [e.rstrip() for e in entries]
card_instances = {k: 1 for k in range(1, len(entries)+1)}

for e in entries:
    card_id, lst = e.split(':')
    id = int(re.findall(r'\d+', card_id)[0])
    winning, actual = lst.split('|')
    winning = re.findall(r'\d+', winning)
    actual = re.findall(r'\d+', actual)
    if (num_winning:= len(set(winning) & set(actual))) > 0:
        #Every copy of the card wins the number of matches, hence add subsequent card instances by multipler
        multiplier = card_instances[id]
        for i in range(1, num_winning+1):
            card_instances[id+i] += (1 * multiplier)

print("Total card instance: ", sum(card_instances.values()))