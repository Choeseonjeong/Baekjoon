def solution(num_list):
    answer = 1
    for i in num_list:
        answer*=i
    num = sum([i for i in num_list])
    num = num*num
    return int(answer<num)