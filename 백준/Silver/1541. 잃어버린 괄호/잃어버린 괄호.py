import sys

n = (sys.stdin.readline().rstrip()).split("-")

result = []
for i in n:
    cnt = 0
    for j in i.split("+"):
        cnt+=int(j)
    result.append(cnt)
answer = result[0]
for i in range(1,len(result)):
    answer-=result[i]
print(answer)
    