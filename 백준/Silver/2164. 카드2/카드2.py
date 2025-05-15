import sys
from collections import deque

n = int(sys.stdin.readline())

arr = deque(range(n, 0, -1))

while len(arr)>1:
    arr.pop()
    arr.appendleft(arr.pop())

print(arr[0])
