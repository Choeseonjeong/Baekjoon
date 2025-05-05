import sys
from collections import Counter

N = int(sys.stdin.readline())
arr1 = (list(sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr2 =  list(sys.stdin.readline().split())

counter = Counter(arr1)

for i in arr2:
    print(counter[i], end=' ')  

