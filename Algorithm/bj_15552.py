import sys

T = sys.stdin.readline()

t = int(T)

list_one = []

for i in range(0, t):
    input_one = sys.stdin.readline()
    splited_one = input_one.split(' ')
    converted_one = [int(i) for i in splited_one]
    list_one.append(converted_one)

sum_all = []

for j in range(0, len(list_one)):
    sum = list_one[j][0] + list_one[j][1]
    sum_all.append(sum)
    
for k in sum_all:
    print(k)