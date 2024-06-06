def solve(a,b):
    count = 0
    for i in map(str, range(a, b)):
        for j in i:
            if j not in '853':
                break
        else: 
            if i.count('8') >= i.count('5') >= i.count('3'): count += 1            
    return count