def solution(s):
    stack = [s[0]]
    for i in range(1,len(s)):
        if stack and stack[-1] != s[i]:
            stack.append(s[i])
        elif stack and stack[-1] == s[i]:
            stack.pop()
        elif not stack:
            stack.append(s[i])
    return 1 if len(stack) == 0 else 0