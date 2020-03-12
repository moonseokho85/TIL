# 거품 정렬(Bubble sort)
# 입력: a
# 출력: 정렬된 리스트

'''
def bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
'''

def bubble_sort(a):
    n = len(a)
    while True: # 정렬이 완료될 때까지 계속 수행
        changed = False # 자료를 앞뒤로 바뀌었는지 여부
        # 자료를 훑어보면서 뒤집힌 자료가 있으면 바꾸고 바뀌었다고 표시
        for i in range(0, n - 1):
            if a[i] > a[i + 1]: # 앞이 뒤보다 크면 
                print(a) # 정렬 과정 추출(참고용)
                a[i], a[i + 1] = a[i + 1], a[i] # 두 자료의 위치를 맞바꿈
                changed = True # 자료가 앞뒤로 바뀌었음을 기록
        # 자료를 한 번 훑어보는 동안 바뀐 적이 없다면 정렬이 완성된 것이므로 종료
        # 바뀐 적이 있으면 다시 앞에서부터 비교 반복
        if changed == False:
            return

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)