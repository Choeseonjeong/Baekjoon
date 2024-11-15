n = int(input())
arr = []
for i in range(n):
    arr=[]
    num = input().split(" ")
    for j in num:
        if int(j)%2==0:
            arr.append(int(j))
    print(sum(arr),min(arr))