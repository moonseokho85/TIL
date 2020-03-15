# 백준 알고리즘 1330번
# 두 수 비교하기
# 입력: 두 정수 A, B
# 출력: A가 B보다 큰 경우에는 '>'를 출력한다.
#       A가 B보다 작은 경우에는 '<'를 출력한다.
#       A와 B가 같은 경우에는 '=='를 출력한다.

# input
n = input()

# split string
splited_n = n.split(' ')

# convert string to int
converted_splited_n = [int(i) for i in splited_n]

# if phrase
if converted_splited_n[0] < converted_splited_n[1]:
    print('<')
elif converted_splited_n[0] > converted_splited_n[1]:
    print('>')
else:
    print('==')