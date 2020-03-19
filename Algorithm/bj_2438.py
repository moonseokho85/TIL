# Baekjun Algorithm No.2438
# Print star
# Input: N
# Output: '*'

import sys
N = sys.stdin.readline()

n = int(N)

for i in range(1, n+1):
    print('*' * i)