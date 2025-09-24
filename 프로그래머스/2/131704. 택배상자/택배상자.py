def solution(order):
    stack = []
    answer = 0
    current = 1
    
    for box in order:
        while current <= box:   # 원하는 상자 나올 때까지 벨트에서 옮김
            stack.append(current)
            current += 1
        if stack[-1] == box:    # 스택 맨 위가 원하는 상자면 꺼냄
            stack.pop()
            answer += 1
        else:                   # 못 꺼내면 더 이상 불가능
            break
    
    return answer
