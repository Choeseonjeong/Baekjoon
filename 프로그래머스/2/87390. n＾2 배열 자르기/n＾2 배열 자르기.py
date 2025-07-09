def solution(n, left, right):
    stack = []
    for i in range(left, right+1):
        a = i%n
        b = i//n
        stack.append(max(a,b)+1)
    return stack