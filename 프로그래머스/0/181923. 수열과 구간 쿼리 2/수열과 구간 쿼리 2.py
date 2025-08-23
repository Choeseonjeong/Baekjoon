def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        num = []
        for i in arr[s:e+1]:
            if i>k:
                num.append(i)
        answer.append(-1 if not num else min(num))
    return answer