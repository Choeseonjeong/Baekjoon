import sys

N = int(sys.stdin.readline())
answer = 0
while answer < N:
    num = map(int,list(str(answer)))
    if answer + sum(num) == N:
        print(answer)
        break
    else:
        answer += 1
if answer >=  N:
    print(0)