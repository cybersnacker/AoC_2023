from pprint import pprint

def parse_input(filepath):
    with open(filepath, 'r') as rf:
        lines = rf.readlines()
    entries = [[w for w in line if w!='\n'] for line in lines]
    return entries

def init_graph(entries):
    graph = {}
    for y, line in enumerate(entries):
        for x, symbol in enumerate(line):
            graph[(x,y)] = []
            graph[(x-0.5, y)] = []
            graph[(x+0.5,y)] = []
            graph[(x,y-0.5)] = []
            graph[(x,y+0.5)] = []

    for y, line in enumerate(entries):
        for x, symbol in enumerate(line):
            match symbol:
                case "-":
                    neighbours = [(x-0.5, y), (x+0.5, y)]
                case "|":
                    neighbours = [(x,y-0.5), (x,y+0.5)]
                case "F":
                    neighbours = [(x+0.5, y), (x,y+0.5)]
                case "J":
                    neighbours = [(x-0.5, y), (x, y-0.5)]
                case "L":
                    neighbours = [(x, y-0.5), (x+0.5, y)]
                case "7":
                    neighbours = [(x-0.5, y), (x, y+0.5)]

            graph[(x,y)] += neighbours
            for neighbour in neighbours:
                graph[neighbour] += [(x,y)]

    return graph

def compute_distances(graph, start_node):
    distance = {}
    dist = 0
    distance[start_node] = 0
    new_nodes = [start_node]

    while new_nodes:
        neighbours = []
        for node in new_nodes:
            neighbours += graph[node]
        new_nodes = []
        dist += 0.5
        for node in neighbours:
            if node not in distance:
                distance[node] = dist
                new_nodes.append(node)

    return distance

        
    
def part1(filepath):
    entries = parse_input(filepath)
    graph = init_graph(entries)
    start_node = (41, 91)
    distance = compute_distances(graph, start_node)
    pprint(distance)
    print(max(distance.values()))

if __name__ == '__main__':
    part1('2023-12-10/input.txt')