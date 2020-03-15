# Baekjun Algorithm No.2884
# Input: Wake up time
# Output: alarm time before 45 minutes

# input
n = input()

# split string
splited_n = n.split(' ')

# convert string to int
converted_splited_n = [int(i) for i in splited_n]

# if phrase
if (converted_splited_n[0] - 1) > 0 and (converted_splited_n[1] - 45) < 0:
    remained_minute = converted_splited_n[1] - 45
    minute = 60 + remained_minute
    converted_splited_n[1] = minute
    converted_splited_n[0] = converted_splited_n[0] - 1
    print(str(converted_splited_n[0]) + ' ' + str(converted_splited_n[1]))
    
elif (converted_splited_n[0] - 1) < 0 and (converted_splited_n[1] - 45) < 0:
    remained_hour = converted_splited_n[0] - 1
    hour = 24 + remained_hour
    converted_splited_n[0] = hour
    remained_minute = converted_splited_n[1] - 45
    minute = 60 + remained_minute
    converted_splited_n[1] = minute
    print(str(converted_splited_n[0]) + ' ' + str(converted_splited_n[1]))
    
else:
    converted_splited_n[1] = converted_splited_n[1] - 45
    print(str(converted_splited_n[0]) + ' ' + str(converted_splited_n[1]))
    