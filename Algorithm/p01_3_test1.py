# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지의 숫자의 제곱을 더한 값

def sum_squared_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i**2
    return s

print(sum_squared_n(10))