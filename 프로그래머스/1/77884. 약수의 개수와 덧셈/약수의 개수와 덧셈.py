def solution(left, right):
    result = 0
    def isPrime(n):
        num = 0
        for i in range(1,n+1):
            if n%i==0:
                num+=1
        return num
    
    for a in range(left, right+1):
        if isPrime(a)%2==0:
            result+=a
        else:
            result-=a
    return result