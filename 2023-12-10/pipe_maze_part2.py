from pprint import pprint
from collections import Counter


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
            neighbours = []
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

def flood_water(graph, seed):

    water = {seed}
    new_nodes = {seed}
    connections = []
    for v in graph.values():
        connections += v
    cntr = Counter(connections)

    while new_nodes:
        tmp_nodes = []
        for (x1, y1) in new_nodes:  # Half-integer nodes
            # Flow down
            if (cntr[(x1, y1+0.5)]) < 2:
                tmp_nodes += [(x1,y1+0.5)]
            # Flow up
            if (cntr[(x1, y1-0.5)]) < 2:
                tmp_nodes += [(x1,y1-0.5)]
            # Flow right
            if (cntr[(x1+0.5, y1)]) < 2:
                tmp_nodes += [(x1+0.5,y1)]
            # Flow left
            if (cntr[(x1-0.5, y1)]) < 2:
                tmp_nodes += [(x1-0.5,y1)]

        new_nodes = set(tmp_nodes).difference(water)
        water.update(new_nodes)

    return water

def water_tiles(entries, water_nodes):
    tiles = []
    for y, line in enumerate(entries):
        for x, symbol in enumerate(line):
            # symbol == "." 
            if all((
                (x-0.5, y-0.5) in water_nodes,
                (x+0.5, y+0.5) in water_nodes,
                (x+0.5, y-0.5) in water_nodes,
                (x-0.5, y+0.5) in water_nodes,
            )):
                tiles.append((x,y))
            
    return tiles


def part2(filepath):
    entries = parse_input(filepath)
    graph = init_graph(entries)
    # pprint(graph)
    connections = []
    for v in graph.values():
        connections += v
    # print(connections)
    # start_node = (41, 91)
    #Do this by hand for input
    start_node = (4 + 0.5, 0 + 0.5)
    start_node = (41 + 0.5, 91 + 0.5)
    # This will give me a list of nodes where water touches
    water_nodes = flood_water(graph, start_node)
    pprint(water_nodes)
    tiles = water_tiles(entries, water_nodes)
    pprint(tiles)
    print(len(tiles))
    # pprint(water_nodes)

if __name__=="__main__":
    part2("2023-12-10/input.txt")
