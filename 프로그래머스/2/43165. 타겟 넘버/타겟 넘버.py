def solution(numbers, target):
    answer = 0
    q = [0] # 첫 시작 값, 저장 값 
    for n in numbers:
        s = [] # 임시 저장 값
        for _ in range(len(q)):
            x = q.pop()
            s.append(x+n)
            s.append(x-n)
        q = s.copy()
    return q.count(target)
        