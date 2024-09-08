sum = int(input())
num = int(input())
result = 0
for i in range(num):
    a, b = list(input().split())
    result += int(a) * int(b)
if sum == result:
    print("Yes")
else:
    print("No")
