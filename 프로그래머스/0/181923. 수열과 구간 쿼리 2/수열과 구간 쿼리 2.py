def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        mid = []
        for i in arr[s:e+1]:
            if i > k: 
                mid.append(i)
        answer.append(-1 if not mid else min(mid))
    return answer