def solution(a, d, included):
    num = 0
    for i in range(len(included)):
        if included[i] == True:
            num += d*(i) + a
    return num