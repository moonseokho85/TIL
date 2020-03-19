# Baekjoon Algorithm No.8393
# Input: n (natural number)
# Output: sum from 1 to n

# input
n = input()

# convert string to int
n = int(n)

sum = 0

for i in range(1, n + 1):
    sum += i
    
print(sum)