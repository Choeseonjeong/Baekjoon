from collections import deque

def solution(priorities, location):
    arr = []
    for idx, num in enumerate(priorities):
        arr.append([idx,num])
    queue = deque(arr)
    stack = []
    while queue:
        idx,pri = queue.popleft()
        if any(pri < k[1] for k in queue):
            queue.append([idx,pri])
        else:
            stack.append([idx,pri])
    answer = 0
    for num in stack:
        answer+=1
        if num[0]==location:
            return answer
        