def solution(n):
    answer = []
    def hanoi(s,m,e,n):
        if n == 1:
            return [[s,e]]
        else: 
            return hanoi(s,e,m,n-1) + [[s,e]] + hanoi(m,s,e,n-1) 

    return hanoi(1,2,3,n)
    