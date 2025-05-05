import sys

N,M = sys.stdin.readline().split()

arr1 = set(list(sys.stdin.readline().split()))
arr2 = set(list(sys.stdin.readline().split()))
print(len(list(arr1-arr2))+len(list(arr2-arr1)))