from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    total = (s1 + s2) 
    count = 0
    limit = len(queue1) * 3 
    
    if total % 2 == 1:
        return -1
    
    while count < limit:
        if s1 == s2:
            return count 
        if s1 > s2:
            val = q1.popleft()
            s1 -= val
            q2.append(val)
            s2 += val
        else:
            val = q2.popleft()
            s2 -= val
            q1.append(val)
            s1 += val
        count += 1
    return -1
            