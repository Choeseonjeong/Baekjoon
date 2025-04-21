n,k = map(int,input().split())
arr = []
for num in range(1,n+1):
    if n % num == 0:
       arr.append(num)

if len(arr)<k: 
    print(0)
else:
    print(arr[k-1])