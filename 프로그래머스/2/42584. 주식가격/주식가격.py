def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for idx,num in enumerate(prices):
        for i in range(idx+1,len(prices)):
            if num > prices[i]:
                answer[idx] = i-idx
                break
            else:
                answer[idx] += 1
    return answer