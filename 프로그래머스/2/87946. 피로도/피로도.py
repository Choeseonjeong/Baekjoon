from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for arr in permutations(dungeons,len(dungeons)):
        temp = k
        count = 0
        for i,j in arr: 
            if temp >= i:
                temp-=j
                count+=1
            else:
                break
        answer = max(answer,count)
    return answer