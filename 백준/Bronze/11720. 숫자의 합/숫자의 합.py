case_num = int(input())
sum=0
num = list(str(input()))
if len(num)==case_num:
    for i in range(case_num):
        sum+=int(num[i])
print(sum)