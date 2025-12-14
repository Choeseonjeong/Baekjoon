def solution(hp):
    cnt = 0
    for num in [5,3,1]:
        d,hp = divmod(hp,num)
        cnt+=d
    return cnt