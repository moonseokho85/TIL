# n번째 피보나치 수 구하기
# 입력: n
# n번째 피보나치 수

def find_number(x):
    a = [0, 1]
    for i in range(100):
        value = a[i] + a[i + 1]
        a.append(value)
    return print(a[x])
        
find_number(5)