def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        n = num[s:s+l]
        if int(n) > k:
            answer.append(int(n))
    return answer