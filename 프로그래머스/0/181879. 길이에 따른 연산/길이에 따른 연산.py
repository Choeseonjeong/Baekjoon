def solution(num_list):
    j = 1
    if len(num_list) >= 11:
        return sum(int(i) for i in num_list)
    else:
        for k in num_list:
            j = int(j) * int(k)
        return j