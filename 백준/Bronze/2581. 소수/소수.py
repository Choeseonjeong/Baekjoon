def is_prime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return n

n = int(input())
m = int(input())
answer = []
result = []

for i in range(n,m+1):
    answer.append(is_prime(i))
for i in range(len(answer)):
    if answer[i] != 0:
        result.append(answer[i])

if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(result[0])

