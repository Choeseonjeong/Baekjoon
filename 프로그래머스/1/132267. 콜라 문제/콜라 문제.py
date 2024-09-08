def solution(a, b, n):
    colla = 0
    result=0
    while n>=a:
        colla+=(n//a)*b
        n=n - (n//a)*a + (n//a)*b
    return colla
        