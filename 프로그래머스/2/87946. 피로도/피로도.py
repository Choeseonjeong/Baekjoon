from itertools import permutations

def solution(k, dungeons):
    all = []
    count = []
    for i in permutations(dungeons, len(dungeons)):
        all.append(i)
    for i in all:
        power = k
        cnt = 0
        for j in i:
            if power >= j[0]:
                power -= j[1]
                cnt +=1 
        count.append(cnt)
        
    return max(count)