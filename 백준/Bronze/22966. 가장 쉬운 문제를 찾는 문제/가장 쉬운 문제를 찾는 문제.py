import sys

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().split() for _ in range(N)]
result = sorted(arr, key = lambda x : x[1])
print(result[0][0])