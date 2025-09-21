def solution(numbers):
    nums = [i for i in range(10)]
    num =0
    for i in nums:
        if i not in numbers:
            num+=i
    return num