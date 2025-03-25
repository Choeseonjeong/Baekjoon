def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        num = int(num[s:s+l])
        if num > k:
            answer.append(num)
    return answer