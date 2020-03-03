# 1부터 n까지의 합 구하기

def sum_fact1(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

print(sum_fact1(1))
print(sum_fact1(5))
print(sum_fact1(10))

def sum_fact2(n):
    if n <= 1:
        return 1
    return n + sum_fact2(n - 1)

print(sum_fact2(1))
print(sum_fact2(5))
print(sum_fact2(10))