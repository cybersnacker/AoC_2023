import numpy as np

def parse_input(filename):
    with open(filename, "r") as fp:
        lines = fp.readlines()

    pattern = []
    for line in lines:
        #Handle multiple pattern blocks in the input file
        if len(line)==1:
            yield np.array(pattern)
            pattern = []
        else:
            pattern.append([c for c in line[:-1]])

    # Yield the last pattern
    yield np.array(pattern)

def mirror_cols(pattern):
    cols = []
    l = pattern.shape[1]
    for mid in range(1, l):
        #Divide the array
        start = 0 if mid <= l//2 else 2*mid - l
        end = l if mid > l//2 else 2*mid
        
        #Keep comparing scanned arrays
        left = pattern[:, start:mid]
        right = pattern[:, end-1:mid-1:-1]
    
        
        if ( left != right ).sum() == 1: 
            # Mid tracks the point of reflection 
            cols.append(mid)

    return cols

ans = 0
for i, pattern in enumerate(parse_input("2023-12-13/examples.txt")):
    cols = mirror_cols(pattern)
    rows = mirror_cols(pattern.T)

    ans += sum(cols) + 100*sum(rows) 

print(ans)
