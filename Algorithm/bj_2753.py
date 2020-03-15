# 백준 알고리즘 2753번
# 윤년
# 입력: 연도
# 출력: 윤년이면 1 아니면 0

# input
n = input()

# convert string to int
year = int(n)

# if phrase
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)