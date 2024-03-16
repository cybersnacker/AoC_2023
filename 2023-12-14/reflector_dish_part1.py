import re
import numpy as np
def parse_input(filepath):
    with open(filepath, 'r') as rf:
        entries = rf.readlines()
    
    l = []
    for e in entries:
        l.append([c for c in e.strip()])
        #l.append(e.strip())
    return np.array(l)

if __name__ == '__main__':
    entries = parse_input('2023-12-14/examples.txt')
    #entries = np.loadtxt('2023-12-14/examples.txt', dtype=str, comments='%')
    print(entries)
    print("--------------------")
    total_load = 0
    count_dict = {}

    N = 1000000000*4
    for n in range(N):
        total_load = 0
        for j in range(entries.shape[0]):
            col_score = -1
            for i in range(entries.shape[1]):
                char = entries[i, j]
                if char == '#':
                    col_score = i
                elif char == 'O':
                    col_score += 1
                    total_load +=  entries.shape[0] - col_score

                    entries[i,j], entries[col_score,j] = entries[col_score,j], entries[i,j]

        entries = np.rot90(entries, -1)
        if n%400000==0: print(100*n/N, f" % ; {total_load=}")
        #print(np.rot90(entries, 1))
        #print("--------------------")   

    #print(entries)           
    print(total_load)
    