def solution(lines):
    answer = {}
    for nums in lines: # [0,1],[2,5]
        for i in range(nums[0], nums[1]): # i = 01,2345
            if i not in answer:
                answer[i]=1
            else:
                answer[i]+=1
    count = 0
    for key, value in answer.items():
        if value>1:
            count+=1
    return count