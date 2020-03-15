# 백준 7568번
# 각 덩치 등수 구하기
# 입력: 5
#       55 185
#       58 183
#       88 186
#       60 175
#       46 155
# 출력: 2 2 1 2 5
'''
def rank():
    
    # input
    n = int(input())
    wah = []
    for i in range(0, n):
        wah.append(input().split(' '))
        # convert string to int
        for j in wah:
            print(j)
    print("wah: ", wah)
    
rank()
'''

N = input()     # 입력값 변수
Answer = []     # 정답에 대한 리스트 변수
Data = []       # 입력을 받은 데이터를 저장하는 리스트 변수

# 데이터를 리스트에 저장하기
for i in range(int(N)):
    list = input().split(" ");
    Data.append(list);    

# 문제를 풀기 위한 알고리즘 ( 2중 반복문 )
for i in range(int(N)):
    count =0;               # 덩치 클 경우 카운트 증가하는 변수
    for j in range(int(N)):
        # 똑같은 데이터는 비교하지 않은다.
        if i == j :
            continue;
        else:       # 데이터가 다른 경우
            if Data[i][0] < Data[j][0] and Data[i][1] < Data[j][1]:
                # 키와 몸무게가 상대방이 둘다 큰 경우 
                count = count + 1;
    Answer.append(count)    # 카운트를 저장
    
string = ""     # 결과 출력 변수
# 결과 포맷에 맞게 출력
for i in range(int(N)):
    print(Answer[i])
    string = string + str(Answer[i]+1) + " "
print(string)    