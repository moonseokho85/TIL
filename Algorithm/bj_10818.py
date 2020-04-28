# Baekjoon Algorithm No.10818
# Input: N, Ns of Integer
# Output: Maximum, Minimum

import sys

##### Input #####
N = sys.stdin.readline() # 1st
Numbers = sys.stdin.readline() # 2nd

##### Convert string to integer type of N #####
n = int(N)

numbers = Numbers.split(' ')
numbers = [int(i) for i in numbers]

##### Extract the min/max value #####
min_value = min(numbers)
max_value = max(numbers)

##### Output #####
print(min_value, max_value)