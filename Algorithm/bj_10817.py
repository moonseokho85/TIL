import sys

# 입력
ABC = sys.stdin.readline()

# 나누기
abc = ABC.split(' ')

# 변환
abc = [int(i) for i in abc]

# 정렬
abc.sort()

# 출력
print(abc[1])