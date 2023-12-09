import re
import math
def parse_input(filename):
    with open(filename, 'r') as rf:
        entries = rf.readlines()
        
    directions = entries[0].rstrip()
    nodes = {}
    for e in entries[2:]:
        key, val = e.split('=')
        nodes[key.rstrip()] = re.findall('\w+', val.strip())
    
    return directions, nodes
    
        
if __name__ == '__main__':
    directions, nodes = parse_input('2023-12-08/input.txt')
    start_nodes = []
    dest_nodes = []
    steps = []
    for k in nodes.keys():
        if k[-1] == 'A':
            start_nodes.append(k)

    for k in nodes.keys():
        if k[-1] == 'Z':
            dest_nodes.append(k)

    for start_node in start_nodes:
        print("Start node: ", start_node)
        dest_node = None
        step = 0
        while dest_node not in dest_nodes:
            for i in directions:
                if i == 'L':
                    dest_node = nodes[start_node][0]
                #print("L: ",dest_node)
                else:
                    dest_node = nodes[start_node][1]
                #print("R: ",dest_node)
                step +=1
            
                start_node = dest_node
                if dest_node in dest_nodes:
                    steps.append(step)
                    print("Dest node: ", dest_node)
                    print("Steps: ", step)
                    break
    print(math.lcm(*steps))


