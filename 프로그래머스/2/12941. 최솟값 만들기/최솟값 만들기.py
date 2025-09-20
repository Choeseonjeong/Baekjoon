def solution(a,b):
    a.sort(reverse=True)
    b.sort(reverse=False)
    num = 0
    for i in range(len(a)):
        num+=a[i]*b[i]
    return num