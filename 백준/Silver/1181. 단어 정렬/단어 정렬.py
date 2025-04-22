n = int(input())
arr = list(set([input() for _ in range(n)]))
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)