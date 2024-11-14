num = 0
arr = []
for i in range(9):
    num = int(input())
    arr.append(num)
max_num = max(arr)
for i in range(len(arr)):
    if arr[i] == max_num:
        print(max_num)
        print(i+1)