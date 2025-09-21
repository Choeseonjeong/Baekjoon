from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons):
        temp = k
        cnt = 0
        for essential, reduce in i:
            if essential <= temp:
                temp -= reduce
                cnt += 1
        answer = max(cnt,answer)
    return answer