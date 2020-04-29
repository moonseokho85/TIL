# Baekjoon Algorithm No.2562
# Input: natural number of 9
# Output: maximum, index

import sys

Numbers = []

# Make list of input
for i in range(9):
    N = sys.stdin.readline() # input
    Numbers.append(N)

# Convert string to integer type of Numbers
numbers = [int(i) for i in Numbers]

# Extract max value
max_value = max(numbers)
print(max_value)

# Extract index of max value
index = numbers.index(max_value) + 1
print(index)