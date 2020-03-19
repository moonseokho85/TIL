# Baekjun Algorithm No.2742
# Input: N
# Output: N부터 1까지 한 줄에 하나씩 출력

import sys

N = sys.stdin.readline()

n = int(N)

for i in range(n, 0, -1):
    print(i)
