def solution(rank, attendance):
    a = [[i,j] for i,j in enumerate(rank)]
    arr = sorted([r for r,a in zip(a, attendance) if a == True],key = lambda x: x[1])
    return arr[0][0]*10000+arr[1][0]*100+arr[2][0]