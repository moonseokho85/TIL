
def print_all_number1(g, start):
    
    qu = []         # 저장 장소 1: 앞으로 처리해야 할 숫자를 큐에 저장
    done = set()    # 저장 장소 2: 이미 큐에 추가된 숫자를 집합에 저장
    
    qu.append(start)    # 자신을 큐에 넣고 시작
    done.add(start)     # 집합에도 추가
    
    while qu:                # 큐에 처리해야 할 숫자가 있는 동안
        p = qu.pop(0)        # 큐에서 처리 대상을 하나 꺼내
        print(p)             # 숫자를 출력
        for x in g[p]:       # 관련 있는 숫자들 중에
            if x not in done:   # 아직 큐에 추가된 적이 없는 숫자를
                qu.append(x)    # 큐에 추가
                done.add(x)     # 집합에도 추가
                
def print_all_number2(g, start):
    
    qu = []
    done = set()
    
    qu.append((start, 0))
    done.add(start)
    
    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)

num_info = {
    '1' : ['2', '3'],
    '2' : ['1', '4', '5'],
    '3' : ['1'],
    '4' : ['2'],
    '5' : ['2']
}

print_all_number1(num_info, '1')
print(' ')
print_all_number2(num_info, '1')
