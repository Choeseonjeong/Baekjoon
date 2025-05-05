import sys

N,M = sys.stdin.readline().split()

arr1 = set(list(sys.stdin.readline().rstrip() for _ in range(int(N))))
arr2 = set(list(sys.stdin.readline().rstrip() for _ in range(int(M))))

cnt = 0
result = sorted(list(arr1&arr2))
print(len(result))
for i in result:
    print(i)