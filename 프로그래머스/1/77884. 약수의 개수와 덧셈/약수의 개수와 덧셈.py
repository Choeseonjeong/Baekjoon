def solution(left, right):
    answer = 0
    def minnum(n):
        arr = []
        for i in range(1,n+1):
            if n%i==0:
                arr.append(i)
        return len(arr)
    for n in range(left, right+1):
        num = minnum(n)
        if num%2 == 0:
            answer+=n
        else:
            answer-=n
    return answer