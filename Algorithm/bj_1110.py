# Baekjoon Algorithm No.1110
# Input: N
# Output: 원래 수로 돌아오는 사이클의 길이

import sys

# 입력
N = sys.stdin.readline()

# int형으로 변환
n = int(N)

# 답을 선언
answer = n

# 사이클의 길이
count = 0

while True:

    if n < 10: # if n = 9
        n = str(0) + str(n) # 09
        converted_n = list(n) # ['0', '9']
        sum = int(converted_n[0]) + int(converted_n[1]) # 9
        sum = str(sum) # '9'
        converted_sum = list(sum) # ['9']
        next_n = converted_n[-1] + converted_sum[-1]
        next_n = int(next_n)
        n = int(n)
        count += 1
        if next_n == answer:
            break
        else:
            n = next_n
    
    else:
        n = str(n)
        converted_n = list(n) # ['9', '9']
        sum = int(converted_n[0]) + int(converted_n[1]) # 9
        sum = str(sum) # '9'
        converted_sum = list(sum) # ['9']
        next_n = converted_n[-1] + converted_sum[-1]
        next_n = int(next_n)
        n = int(n)
        count += 1
        if next_n == answer:
            break
        else:
            n = next_n
            
print(count)