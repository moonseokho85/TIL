# n번째 피보나치 수열 구하기
# 입력: n
# n번째 피보나치 수

def find_number(n):
    a = [0, 1]
    for i in range(100):
        value = a[i] + a[i + 1]
        a.append(value)
    return print(a[n])
        
find_number(5)

# n번째 피보나치 수열 찾기 (재귀 용법)
# 입력: n 값(0부터 시작)
# 출력: n번째 피보나치 수열 값

def fibo(n):
    if n <= 1:
        return n # n = 0 -> 0 | n = 1 -> 1
    return fibo(n - 2) + fibo(n - 1)

print(fibo(7))
print(fibo(10))