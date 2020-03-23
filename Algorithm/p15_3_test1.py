
def print_all_number1(g, start):
    
    qu = []
    done = set()
    
    qu.append(start)
    done.add(start)
    
    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
                
def print_all_number2(g, start):
    
    qu = []
    done = set()
    
    qu.append((start, 0))
    done.add(start)
    
    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)

num_info = {
    '1' : ['2', '3'],
    '2' : ['1', '4', '5'],
    '3' : ['1'],
    '4' : ['2'],
    '5' : ['2']
}

print_all_number1(num_info, '1')
print(' ')
print_all_number2(num_info, '1')
