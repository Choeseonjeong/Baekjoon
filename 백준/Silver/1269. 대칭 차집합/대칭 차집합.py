import sys
input = sys.stdin.readline

N,M = map(int,input().split())
S_a = set(map(int, input().split()))
S_b = set(map(int, input().split()))
print(len(S_a - S_b) + len(S_b - S_a))