def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else: # i==")"
            if len(stack)==0:
                return False
            else:
                stack.pop()
    return False if stack else True