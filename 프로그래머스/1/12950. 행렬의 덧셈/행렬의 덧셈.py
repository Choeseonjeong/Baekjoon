def solution(arr1, arr2):
    answer = []
    n,m = len(arr1),len(arr1[0])
    
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer