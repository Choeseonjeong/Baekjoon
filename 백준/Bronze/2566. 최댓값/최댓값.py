matrix = []
for _ in range(9):
    row = list(map(int,input().split()))
    matrix.append(row)

maxNum = 0
a,b = 0,0
for i in range(9):
    for j in range(9):
        if matrix[i][j]>=maxNum:
            maxNum = matrix[i][j]
            a = i
            b = j
print(maxNum)
print(a+1,b+1)