def solution(n, arr1, arr2):
    def twoDemical(arr):
        num1 = []
        for i in arr:
            a = bin(i)[2:]
            a = '0' * (n - len(a)) + a
            num1.append(list(a))  
        return num1
    
    num1 = twoDemical(arr1)
    num2 = twoDemical(arr2)
    
    result = []
    for i in range(n):
        temp = ""
        for j in range(n):
            if num1[i][j] == "1" or num2[i][j] == "1":
                temp += "#"
            else:
                temp += " "
        result.append(temp)
    return result



