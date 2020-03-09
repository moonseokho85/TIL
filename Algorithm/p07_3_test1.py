# 학생 번호에 따른 이름을 반환해주는 함수
# input: n
# output: 번호에 따른 이름

def find_name(a, b, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return b[i]
    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(find_name(stu_no, stu_name, 39))