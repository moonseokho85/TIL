# Baekjun Algorithm No.2739
# Input: N
# Output: print from N * 1 to N * 9

# input
N = input()

# convert string to int
N = int(N)

# print
for i in range(1, 10):
    result = N * i
    print(N, '*', i, '=', result)