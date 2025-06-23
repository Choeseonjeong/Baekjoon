def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == "(":
                stack.append(i)
            else:
                stack.pop()    
    return True if not stack else False