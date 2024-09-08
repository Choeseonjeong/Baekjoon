def solution(x):
    answer=0
    arr=list(str(x))
    for i in arr:
        answer+=int(i)
    if x%answer==0:
        return True
    else:
        return False
    