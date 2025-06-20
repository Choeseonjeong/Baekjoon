import sys



N = int(sys.stdin.readline())
answer = 2

for _ in range(N):
    answer = answer + (answer-1)
print(answer*answer)
