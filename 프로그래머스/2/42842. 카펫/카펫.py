def solution(brown, yellow):
    arr = []
    for x in range(1,brown+1):
        for y in range(1,brown+1):
            if x*y == brown+yellow:
                arr.append([x,y])
    result = []
    for i, j in arr:
        if (i-2) * (j-2) == yellow:    
            return [i, j] if i >= j else [j, i]
