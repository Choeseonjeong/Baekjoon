def solution(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                n = nums[i] + nums[j] + nums[k]
                if n < 2:
                    continue
                for d in range(2, int(n**0.5) + 1):
                    if n % d == 0:
                        break
                else:
                    count += 1
    return count
