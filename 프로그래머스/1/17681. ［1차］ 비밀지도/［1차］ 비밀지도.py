def solution(n, arr1, arr2):
    cnt=[]
    for i in range((n)):
        num = (bin((arr1[i])|(arr2[i]))[2:]) # 비트연산자 : |
        num = num.zfill(n)
        result = num.replace("1","#").replace("0"," ")
        cnt.append(result)
    return cnt
