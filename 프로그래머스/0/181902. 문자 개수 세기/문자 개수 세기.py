def solution(my_string):
    answer = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    num = [0]*52
    nums = {}
    for key, value in zip(answer, num):
        nums[key] = value
    for i in my_string:
        nums[i]+=1
    result = []
    for i in nums:
        result.append(nums[i])
    return result
