# 찾는 값이 나오는 모든 위치
# 입력: 리스트 a, 리스트 x
# 출력: 찾으면 그 값의 위치들, 찾지 못하면 []

def search_list(a, x):
    n = len(a)
    return_list = []
    for i in range(0, n):
        