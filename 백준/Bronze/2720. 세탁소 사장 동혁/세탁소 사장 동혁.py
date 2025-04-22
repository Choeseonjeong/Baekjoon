n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
# 값 입력

# 머니 입력 함수
def money(n,m):
    count = 0
    while n >= m:
        n -= m
        count+=1
    return n,count
    
for i in arr:
    n,count = money(i,25)
    print(count, end=' ')
    n,count = money(n,10)
    print(count, end=' ')
    n,count = money(n,5)
    print(count, end=' ')
    n,count = money(n,1)
    print(count)
    