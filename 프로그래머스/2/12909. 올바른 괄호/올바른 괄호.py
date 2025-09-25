def solution(s):
    answer = True
    stack = []
    for word in s:
        if not stack: 
            stack.append(word)
        elif stack and word == "(":
            stack.append(word)
        elif stack and word==")":
            stack.pop()
    return True if len(stack)==0 else False