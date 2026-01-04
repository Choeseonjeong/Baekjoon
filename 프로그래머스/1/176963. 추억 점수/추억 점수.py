def solution(name, yearning, photo):
    answer = []
    arr = {}
    for n,y in zip(name,yearning):
        arr[n] = y
    
    for a in photo:
        num = 0
        for b in a:
            if b in arr:
                num += arr[b]
            else:
                num+=0
        answer.append(num)
    return answer