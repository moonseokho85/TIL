# Baekjoon Algorithm No.10039
# Input: 점수
# Output: 조건식에 따른 평균 성적

import sys

grades = []

for i in range(0, 5):
    point = sys.stdin.readline()
    point = int(point)
    
    # 점수가 40점 이상이면
    if point >= 40:
        # 그대로 성적으로 저장
        grade = point
    # 점수가 40 미만이면
    else:
        # 40점을 성적으로 저장
        grade = 40
        
    grades.append(grade)

average = sum(grades, 0) / len(grades)
print(int(average))