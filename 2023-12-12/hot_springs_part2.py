import numpy as np

def parse_input(filepath):
    """
    Returns a dictionary of entries and groupings
    """
    with open(filepath, 'r') as rf:
        lines = rf.readlines()
    
    entries = [l.strip().split(' ')[0] for l in lines]
    groups = [l.strip().split(' ')[1] for l in lines]
    return dict(zip(entries, groups))

def match(chars, start, end):
    for i in range(start, end, 1):
        if(chars[i] == '.'):
            return False
    return True

def count_arrangements(chars, springs):
    n = len(chars)
    m = len(springs)
    #dp[i][j] stores how many arrangements when matching [i..n-1] chars with [j..m-1] springs
    # Modeled like the LCS problem
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    dp[n][m] = 1;

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            val = 0
            if springs[j] > 0:
                end = i + springs[j]
                if match(chars, i, end):
                    val = dp[end][j+1]
            elif chars[i] != '#':
                val =  dp[i+1][j+1] + dp[i+1][j]
            dp[i][j] = val
        #print(f"DP State for char {i}: {dp[i][j]}")

    #print(f"Arrangements for {chars}: {dp[0][0]}")
    return dp[0][0]


if __name__ == '__main__':
    entries_dict = parse_input('2023-12-12/input.txt')
    #print(entries, groups)
    sum_of_arrangements = 0

    for e ,g in entries_dict.items():
        print(e, g)
        multiplied_e = (e+'?') * 5
        print(multiplied_e)
        g = [int(x) for x in g.split(',')]
        multiplied_g = g * 5
        padded_e = '.'+multiplied_e+'.'
        #Add -1 for padding and to delineate groups of springs
        for index, item in enumerate(multiplied_g):
            if index %2 ==1:
                multiplied_g.insert(index, -1)
        multiplied_g.insert(0, -1)
        multiplied_g.extend([-1])
        arrangements = count_arrangements(padded_e, multiplied_g)
        sum_of_arrangements += arrangements
        print(f"Arrangements for {e, g}: {arrangements}")


    print('Sum:', sum_of_arrangements) 