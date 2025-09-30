def solution(s):
    stack = []
    for i in s:
        if stack and i=="(":
            stack.append(i)
        elif not stack:
            stack.append(i)
        elif stack and i==")" and stack[-1]=="(":
            stack.pop()
    return False if len(stack)!=0 else True