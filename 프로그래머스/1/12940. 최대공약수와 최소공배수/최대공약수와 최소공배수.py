def solution(n, m):
    def gcd(n,m):
        while m>0:
            n,m = m,n%m
        return n
    def lcd(n,m):
        return (n*m//gcd(n,m))
    return [gcd(n,m),lcd(n,m)]


