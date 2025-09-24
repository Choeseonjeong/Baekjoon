def solution(n):
    answer = 0
    def isprime(num):
        if num < 2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    count = 0
    for num in range(1,n+1):
        if isprime(num):
            count+=1
    return count
            