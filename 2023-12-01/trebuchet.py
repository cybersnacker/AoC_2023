with open("input.txt", 'r') as rf:
    entries = rf.readlines()

sum_of_entries = 0

spelling_digit_map = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
    "zero": '0'
}

entries = [[*(e.rstrip())] for e in entries]

#For Part 2
for e in entries:
    #print("Before substitution:", ''.join(e))
    for pos in range(len(e)-2):
        for i in range(3, 6, 1):
            if (substring := "".join(e[pos:pos+i])) in spelling_digit_map.keys():
                e[pos] = spelling_digit_map[substring]         

# Part 1 only solution
for e in entries:
    tenths_place = 0
    ones_place = 0
    for c in e:
        if c.isdigit():
            tenths_place = c
            break
    
    for c in e[::-1]:
        if c.isdigit():
            ones_place = c
            break

    num_e = int(tenths_place) * 10 + int(ones_place)
    #print("After substitution: ", ''.join(e), num_e)
    with open('our_soln.txt', 'a') as wf:
        wf.write(str(num_e)+"\n")

    sum_of_entries+= num_e
print(sum_of_entries)

