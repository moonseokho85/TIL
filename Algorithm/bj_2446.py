# Baekjun Algorithm No.2446
# Print star
# Input: N
# Output: '*'

import sys

# 입력
N = sys.stdin.readline()

# int형으로 변환
n = int(N)

# 2n - 1까지 출력
converted_n = 2 * n - 1

star = ''

for i in range(1, converted_n + 1):
    # for문의 i가 n보다 작거나 같으면
    if i <= n:
        # 별을 더해준다
        star += '*'
    # 아니면
    else:
        # 별을 빼준다
        star = star[:-1]
    print(star)