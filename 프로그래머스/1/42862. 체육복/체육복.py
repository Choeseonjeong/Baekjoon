def solution(n, lost, reserve):
    lost_set = set(lost)
    lost_res = set(reserve)
    both = lost_set & lost_res
    lost_set-=both
    lost_res-=both
    
    for i in sorted(lost_res):
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    return n - len(lost_set)     