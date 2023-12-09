import re
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
    #print(directions, nodes)
    start_node = 'AAA'
    dest_node = None
    step = 0
    
    while dest_node != 'ZZZ':
        for i in directions:
            if i == 'L':
                dest_node = nodes[start_node][0]
            else:
                dest_node = nodes[start_node][1]
            step +=1
            start_node = dest_node
            if dest_node == 'ZZZ':
                break
    print(step)
