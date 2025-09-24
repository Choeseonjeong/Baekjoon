import math

def solution(n, k):
    nums = [i for i in range(1,n+1)]
    answer = []
    k -= 1
    for i in range(n,0,-1):
        f = math.factorial(i-1)
        idx = k//f
        k %= f
        answer.append(nums.pop(idx))
    return answer