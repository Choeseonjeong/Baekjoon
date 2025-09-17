def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        num = queue.pop(0)
        if any(num[1] < cur[1] for cur in queue):
            queue.append(num)
        else:
            answer += 1
            if num[0] == location:
                return answer
            