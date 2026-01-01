from collections import Counter

def solution(array):
    nums = Counter(array)
    max_count = max(nums.values())
    answer = [k for k,v in nums.items() if max_count == v]
    return answer[0] if len(answer)==1 else -1