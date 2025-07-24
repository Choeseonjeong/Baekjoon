import itertools # 모든 조합

# 최대 돌 수 있는 던전 수 / 모두 돌아야 함
def solution(k, dun):
    per_dun = list(itertools.permutations(dun))
    total = []
    
    for dun in per_dun:
        num = 0
        k_copy = k 
        for need_stress, stress in dun:
            if k_copy < need_stress:
                break
            else:
                k_copy -= stress
                num += 1
        total.append(num)
    return max(total)