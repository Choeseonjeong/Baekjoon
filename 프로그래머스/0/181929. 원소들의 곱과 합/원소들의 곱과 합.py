from functools import reduce

def solution(num_list):
    n = len(num_list)
    j = sum(num_list)*sum(num_list)
    k = reduce(lambda x,y : x*y, num_list)

    if j>k :return 1
    else: return 0