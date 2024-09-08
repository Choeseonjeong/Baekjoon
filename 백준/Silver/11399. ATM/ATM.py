n = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()

total_time = 0
personal_time = 0
for i in arr:
    personal_time += i
    total_time += personal_time
print(total_time)
