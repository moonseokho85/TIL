import sys

N = sys.stdin.readline()

n = int(N)

answer = n

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