# 백준 알고리즘 9498번
# 입력받은 점수의 학점을 출력해주는 프로그램
# 입력: 시험 점수
# 출력: 시험 성적

# input
n = input()

# convert string to int
point = int(n)

# if phrase
if 90 <= point <= 100:
    print('A')
elif 80 <= point <= 89:
    print('B')
elif 70 <= point <= 79:
    print('C')
elif 60 <= point <= 69:
    print('D')
else:
    print('F')