# Baekjun Algorithm No.10950
# Input: T, A, B
# Output: A + B

# input testcase count
T = input()

# convert string to int
t = int(T)

input_list = []
for i in range(0, t):
    input_a = input()
    input_a = input_a.split(' ')
    input_a = [int(i) for i in input_a]
    input_list.append(input_a)
    
output_list = []
for j in input_list:
    output_a = (j[0] + j[1])
    output_list.append(output_a)

for k in output_list:
    print(k)