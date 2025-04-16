a, b = map(int, input().split())

matrix1 = []
matrix2 = []
matrixSum = []
for i in range(a):
    matrix1.append(list(map(int, input().split())))

for i in range(a):
    matrix2.append(list(map(int, input().split())))
    
    
for i in range(a):
    row = []
    for j in range(b):
        print(matrix1[i][j] + matrix2[i][j], end=' ')
    print()