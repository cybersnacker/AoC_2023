import re
import numpy as np

def parse_input(filename):
    with open(filename, 'r') as rf:
        entries = rf.readlines()
        
    directions = entries[0].rstrip()
    nodes = {}
    for e in entries[2:]:
        key, val = e.split('=')
        nodes[key.rstrip()] = re.findall('\w+', val.strip())
    
    return directions, nodes

def get_adjacency_matrices(nodes, pos_dict):
    L = np.zeros((len(nodes), len(nodes)))
    R = np.zeros((len(nodes), len(nodes)))

    for k, (l,r) in nodes.items():
        L[pos_dict[l], pos_dict[k]] = 1
        R[pos_dict[r], pos_dict[k]] = 1
    
    return L, R

def build_matrices(nodes, pos_dict):
    start_state = np.zeros(len(nodes), dtype=int)
    for num, key in enumerate(nodes):
        # if key == "AAA":
        #     start_state[num] = 1
        if key[-1] == 'A':
            start_state[num] = 1

    end_state = np.zeros(len(nodes), dtype=int)
    for num, key in enumerate(nodes):
        # if key == 'ZZZ':
        #     end_state[num] = 1
        if key[-1] == 'Z':
            end_state[num] = 1

    left_matrix, right_matrix = get_adjacency_matrices(nodes, pos_dict)
    return start_state, end_state, left_matrix, right_matrix
        
if __name__ == '__main__':
    directions, nodes = parse_input('2023-12-08/examples_3.txt')
    pos_dict = {}
    for pos, key in enumerate(nodes):
        pos_dict[key] = pos
    start, end, left_m, right_m = build_matrices(nodes, pos_dict)
    # print(start.sum(), end.sum())
    # exit()
    #print(start, end, left_m, right_m)

    current = start
    step = 0
    while not (current == end).all():
        for i in directions:
            if i == 'L':
                current = np.matmul(left_m, current)
            else:
                current = np.matmul(right_m, current)
            step += 1
            if step % 100000 == 0:
                print(step)
            if (current == end).all():
                break
    
    print(step)

