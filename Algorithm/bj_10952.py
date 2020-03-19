# Baekjoon Algorithm No.10952
# Input: A B
# Output: A + B

# import
import sys

# declare the list
sum_all = []

# while phrase
while True:
    # input
    AB = sys.stdin.readline()
    
    # split the string
    splited_AB = AB.split(' ')
    
    # convert string to int
    converted_AB = [int(i) for i in splited_AB]
    
    # if input is 0, while phrase break
    if converted_AB[0] == 0 and converted_AB[1] == 0:
        for j in range(0, len(sum_all)):
            print(sum_all[j])
        break
    
    sum = converted_AB[0] + converted_AB[1]
    sum_all.append(sum)