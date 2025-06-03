import sys

N = int(sys.stdin.readline())
arr = sorted(map(int,sys.stdin.readline().split()))
print(int(arr[0])*int(arr[-1]))