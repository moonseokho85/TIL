import sys

N = sys.stdin.readline()

n = int(N)

while True:

    if n < 10: # if n = 9
        print("n < 10")
        n = str(0) + str(n) # 09
        converted_n = list(n) # ['0', '9']
        sum = int(converted_n[0]) + int(converted_n[1]) # 9
        sum = str(sum) # '9'
        converted_sum = list(sum) # ['9']
        next_n = converted_n[-1] + converted_sum[-1]
        next_n = int(next_n)
        if next_n == n:
            break
        else:
            next_n = n
    
    else:
        print("n > 10")
        n = str(n)
        converted_n = list(n) # ['9', '9']
        sum = int(converted_n[0]) + int(converted_n[1]) # 9
        sum = str(sum) # '9'
        converted_sum = list(sum) # ['9']
        next_n = converted_n[-1] + converted_sum[-1]
        next_n = int(next_n)
        if next_n == n:
            break
        else:
            next_n = n