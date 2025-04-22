def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
m = int(input())
answer = [i for i in range(n,m+1) if is_prime(i)]



if len(answer)==0:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])

