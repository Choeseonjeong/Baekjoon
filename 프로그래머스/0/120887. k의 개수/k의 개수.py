def solution(i, j, k):
    arr = []
    count = 0
    for num in range(i,j+1):
        for j in range(len(str(num))):
            arr.append(str(num)[j])
    return arr.count(str(k))