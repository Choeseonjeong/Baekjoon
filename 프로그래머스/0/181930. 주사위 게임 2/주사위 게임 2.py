def solution(a, b, c):
    if a == b and b == c and c == a:
        return (a+b+c)*(a*a+b*b+c*c)*(a**3+b**3+c**3)
    elif a != b and b!=c and c!=a:
        return a+b+c
    else:
        return (a+b+c)*(a*a+b*b+c*c)
    