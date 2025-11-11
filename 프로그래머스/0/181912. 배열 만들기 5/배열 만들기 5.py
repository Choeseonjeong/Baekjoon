def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        n = num[s:s+l]
        if k < int(n):
            answer.append(int(n))
    return answer