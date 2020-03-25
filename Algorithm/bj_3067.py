import sys

T = sys.stdin.readline()

t = int(T)

for i in range(0, t):
    
    N = sys.stdin.readline()
    
    n = int(N)
    
    for j in range(0, 2):
        
        kinds = sys.stdin.readline()
        
        M = sys.stdin.readline()
        
        splited_kinds = kinds.split(' ')
        
        converted_kinds = [int(i) for i in splited_kinds]
        
        m = int(M)
        
        for k in range(0, n):
            
        
        