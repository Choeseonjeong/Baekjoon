n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

x = [arr[i][0] for i in range(len(arr))]
y = [arr[i][1] for i in range(len(arr))]

print((max(x)-min(x))*(max(y)-min(y)))