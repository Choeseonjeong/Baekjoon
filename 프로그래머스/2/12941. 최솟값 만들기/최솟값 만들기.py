
def solution(a, b):
    a.sort()
    b.sort(reverse=True)

    return sum(a[i] * b[i] for i in range(len(b)))
