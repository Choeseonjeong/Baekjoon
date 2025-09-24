def solution(n, arr1, arr2):
    result = []
    def maps(arr):
        num1 = []
        for i in arr:
            num = bin(i)[2:]
            if len(num)<n:
                num = "0"*(n-len(num))+num
            num1.append(num)
        return num1
    ans1 = maps(arr1)
    ans2 = maps(arr2)
    
    for i in range(n):
        ch = ''
        for j in range(n):
            if ans1[i][j]=="1" or ans2[i][j]=="1":
                ch += "#"
            else:
                ch += " "
        result.append(ch)
    return result