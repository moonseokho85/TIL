# 학생 번호에 따른 이름을 반환해주는 함수
# input: n
# output: 번호에 따른 이름

def find_name(a, b, x):
    n = len(a) # 입력크기 n
    for i in range(0, n): 
        if x == a[i]: # 학생 번호가 찾는 학생 번호와 같으면
            return b[i] # 해당하는 학생 이름을 결과로 반화
    return '?' # 자료를 다 뒤져서 못 찾았으면 물음표 반환

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(find_name(stu_no, stu_name, 39))
print(find_name(stu_no, stu_name, 888))