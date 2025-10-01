def solution(s):
    answer = [-1 for _ in range(len(s))]
    stack = []
    for idx, text in enumerate(s):
        for s in range(len(stack)-1,-1,-1):
            if stack and stack[s] == text:
                answer[idx] = idx - s
                break
        stack.append(text)
    return answer