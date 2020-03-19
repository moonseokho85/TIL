# Baekjun Algorithm No.11021
# Input: T, A, B
# Output: A + B

import sys
T = sys.stdin.readline()

t = int(T)

a = []

for i in range(0, t):
    input_a = sys.stdin.readline()
    splited_a = input_a.split(' ')
    converted_a = [int(i) for i in splited_a]
    a.append(converted_a)
    
sum_all = []

for j in range(0, len(a)):
    sum = a[j][0] + a[j][1]
    sum_all.append(sum)

for k in range(0, len(sum_all)):
    print('Case #' + str(k+1) + ': ' + str(sum_all[k]))