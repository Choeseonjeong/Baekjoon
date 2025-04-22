arr = []
for i in range(3):
    arr.append(list(map(int,input().split())))
arr1 = [arr[i][0] for i in range(len(arr))]
arr2 = [arr[i][1] for i in range(len(arr))]

for i in arr1:
    if arr1.count(i)==1:
        n = i
for i in arr2:
    if arr2.count(i)==1:
        m = i
print(n,m)