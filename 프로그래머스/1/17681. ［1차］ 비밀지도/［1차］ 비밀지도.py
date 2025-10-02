def solution(n, arr1, arr2):
    answer = []
    for idx,(a,b) in enumerate(zip(arr1,arr2)):
        ar1 = bin(a)[2:] if len(bin(a)[2:]) == n else (n-len(bin(a)[2:]))*str(0)+bin(a)[2:]
        ar2 = bin(b)[2:] if len(bin(b)[2:]) == n else (n-len(bin(b)[2:]))*str(0)+bin(b)[2:]
        row = ''
    
        for i,j in zip(ar1,ar2):
            if i == "1" or j == "1": 
                row+="#"
            else:
                row+= " "
        answer.append(row)
    return answer