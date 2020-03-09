# 찾는 값이 나오는 모든 위치
# 입력: 리스트 a, 리스트 x
# 출력: 찾으면 그 값의 위치들, 찾지 못하면 []

def search_list(a, x):
    n = len(a)
    result = []
    for i in range(0, n):    
        if x == a[i]:
            result.append(i)
    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(search_list(v, 18))   # [2] (순서상 세 번째지만, 위치 번호는 2)
print(search_list(v, 33))   # [3, 6] (33은 리스트에 두 번 나옴)
print(search_list(v, 900))  # [ ] (900은 리스트에 없음)