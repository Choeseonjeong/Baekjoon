def solution(n):
    answer = 0
    while answer < 500 and n!=1:
        answer+=1
        if n%2==0:
            n/=2
        else:
            n = n*3+1
        if n==1:
            break

    return -1 if answer == 500 else answer