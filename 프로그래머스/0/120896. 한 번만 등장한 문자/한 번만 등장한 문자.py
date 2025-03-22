def solution(s):
    arr = []
    answer = ''
    for i in list(s):
        arr.append(i)
    arr.sort()
    for i in arr:
        if arr.count(i)<2:
            answer+=i
    return answer
            