def solution(s):
    stack = []
    for text in s:
        if text == "(":
            stack.append(text)
        else: # ) 인 경우 
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
                
        
            