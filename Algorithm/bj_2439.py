# Baekjun Algorithm No.2438
# Print star in right align
# Input: N
# Output: '*'

import sys
N = sys.stdin.readline()

n = int(N)

for i in range(1, n+1):
    print(' ' * (n - i) + '*' * i)