# Baekjoon Algorithm No.2577
# Input: A, B, C
# Output: each number of 0 ~ 9

import sys

Numbers = []

# Making list of input
for i in range(3):
    N = sys.stdin.readline() # input
    Numbers.append(N)

# Converting string to integer type of Numbers
numbers = [int(i) for i in Numbers]

# Multipling all of numbers parameters
sum_numbers = numbers[0] * numbers[1] * numbers[2]

# Spliting the sum_numbers
splitted_sum_numbers = list(str(sum_numbers))

# Converting string to integer type of splitted_sum_numbers
splitted_sum_numbers = [int(i) for i in splitted_sum_numbers]
print(splitted_sum_numbers)

dictionary = {x:splitted_sum_numbers.count(x) for x in splitted_sum_numbers}
print(dictionary)
