# Baekjun Algorithm No.10871
# Print star
# Input: N, X, Sequence A
# Output: X보다 작은 수

import sys

# input
NX = sys.stdin.readline()
A = sys.stdin.readline()

# split the NX to N and X
splited_NX = NX.split(' ')
splited_A = A.split(' ')

# convert string to int
converted_NX = [int(i) for i in splited_NX]
converted_A = [int(i) for i in splited_A]

# declare the list
answer = []

for i in range(0, len(converted_A)):
    # 수열 A의 값이 X보다 작으면
    if converted_A[i] < converted_NX[1]:
        answer.append(converted_A[i])

# convert int to string
str_answer = [str(i) for i in answer]

print(' '.join(str_answer))
