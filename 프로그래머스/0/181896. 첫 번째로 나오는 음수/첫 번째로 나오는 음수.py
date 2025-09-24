def solution(num_list):
    answer = 0
    for idx, num in enumerate(num_list):
        if num<0:
            return idx
    return -1